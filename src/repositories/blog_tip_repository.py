from entities.blog_tip import BlogTip
from repositories.database_connection import get_connection

class BlogTipRepository:
    def __init__(self, connection=get_connection()):
        self._connection = connection
        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Blogtips (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author TEXT,
                url TEXT,
                read INTEGER
            );
        """)

        connection.commit()

    def add(self, blog_tip):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BlogTips WHERE url=?", (blog_tip.url,))

        result = cursor.fetchone()

        if result:
            return

        cursor.execute("INSERT INTO Blogtips (name, author, url, read) VALUES (?, ?, ?, ?)",
            (blog_tip.name, blog_tip.author, blog_tip.url, 0))

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Blogtips")

        rows = cursor.fetchall()

        return [BlogTip(row["name"], row["author"], row["url"], row["id"], bool(row["read"]))
                for row in rows]

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from Blogtips')

        self._connection.commit()

    def drop_tables(self):
        cursor = self._connection.cursor()

        cursor.execute("""
            DROP TABLE IF EXISTS Blogtips;
        """)

        self._connection.commit()

    def mark_as_read(self, id_number):
        cursor = self._connection.cursor()
        try:
            cursor.execute("UPDATE Blogtips SET read = 1 WHERE id = ?", (id_number))
            self._connection.commit()
            return True
        except:
            return False
    

    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders=['ASC']):
        if not fields: return []
        values = [x.lower() for x in values]
        if not sortByValues: sortByValues.append(fields[0])
        if not comparators: comparators.append('=')

        search_string = "SELECT * FROM Blogtips " + self.where_string(fields, comparators) + self.order_string(sortByValues, sortbyOrders)+";"
        print(search_string)

        k=0
        while k < len(comparators):
            if comparators[k].upper().strip()=='LIKE': values[k] = "%" + values[k] + "%"
            k += 1

        cursor = self._connection.cursor()
        
        rows = cursor.execute(search_string, values)

        rows = cursor.fetchall()

        return [BlogTip(
            row["name"],
            row["author"],
            row["url"])
            for row in rows]


    def where_string(self, fields, comparators):
        if not fields: return ""
        where_string = "WHERE lower(" + fields[0].lower() + ")" + comparators[0].upper() + "?"

        i=1
        while i < len(fields):
            comparator = comparators[0].upper()
            if i < len(comparators): comparator = comparators[i].uppper()
            where_string +=  " AND lower("+ fields[i].lower() + ")" + comparator.upper() + "?"
            i += 1
        return where_string
    

    def order_string(self, sortByValues, sortbyOrders):
        if not sortByValues: return ""
        order_string = " ORDER BY " + sortByValues[0].lower() + " " + sortbyOrders[0].upper()

        j=1
        while j < len(sortByValues):
            order_string += ", " + sortByValues[j].lower() + " " + sortbyOrders[j].upper()
            j += 1
        return order_string
    
    
    
    
    
    '''
    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders=['ASC']):
        if not fields: return []
        values = [x.lower() for x in values]
        if not sortByValues: sortByValues.append(fields[0])
        if not comparators: comparators.append('=')

        search_string = "SELECT * FROM Blogtips WHERE lower(" + fields[0].lower() + ")" + comparators[0]+"?"
        
        i=1
        while i < len(fields):
            comparator = comparators[0]
            if i < len(comparators): comparator = comparators[i]
            search_string += " AND lower(" + fields[i].lower() + ")" + comparator+ "?"
            i += 1
        
        search_string += " ORDER BY " + sortByValues[0].lower() + " " + sortbyOrders[0].upper()

        j=1
        while j < len(sortByValues):
            search_string += ", " + sortByValues[j].lower() + " " + sortbyOrders[j].upper()
            j += 1
        search_string += ";"

        cursor = self._connection.cursor()

        rows = cursor.execute(search_string, values)

        rows = cursor.fetchall()

        return [BlogTip(
            row["name"],
            row["author"],
            row["url"])
            for row in rows]
    '''


