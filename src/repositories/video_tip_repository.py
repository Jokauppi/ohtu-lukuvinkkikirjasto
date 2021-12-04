from entities.video_tip import VideoTip
from repositories.database_connection import get_connection

class VideoTipRepository:
    def __init__(self, connection=get_connection()):
        self._connection = connection
        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Videotips (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT,
                read INTEGER
            );
        """)

        connection.commit()

    def add(self, video_tip):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM VideoTips WHERE url=?", (video_tip.url,))

        result = cursor.fetchone()

        if result:
            return

        cursor.execute("INSERT INTO Videotips (title, url, read) VALUES (?, ?, ?)",
            (video_tip.title, video_tip.url, 0))

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Videotips")

        rows = cursor.fetchall()

        return self.to_list(rows)
    
    def get_read(self, read):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Videotips WHERE read=?", (read,))

        rows = cursor.fetchall()

        return self.to_list(rows)

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from Videotips')

        self._connection.commit()

    def drop_tables(self):
        cursor = self._connection.cursor()

        cursor.execute("""
            DROP TABLE IF EXISTS Videotips;
        """)

        self._connection.commit()

    def mark_as_read(self, id_number):
        cursor = self._connection.cursor()
        try:
            cursor.execute("UPDATE Videotips SET read = 1 WHERE id = ?", (id_number))
            self._connection.commit()
            return True
        except:
            return False
    

    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders=['ASC']):
        if not fields: return self.get_all()
        values = [x.lower() for x in values]
        if not sortByValues: sortByValues.append(fields[0])
        if not comparators: comparators.append('=')

        search_string = "SELECT * FROM Videotips " + self.where_string(fields, comparators) + self.order_string(sortByValues, sortbyOrders)+";"

        k=0
        while k < len(comparators):
            if comparators[k].upper().strip()=='LIKE': values[k] = "%" + values[k] + "%"
            k += 1

        cursor = self._connection.cursor()
        
        cursor.execute(search_string, values)

        rows = cursor.fetchall()

        return self.to_list(rows)


    def where_string(self, fields, comparators):
        if not fields: return ""
        where_string = "WHERE lower(" + fields[0].lower() + ")" + comparators[0].upper() + "?"

        i=1
        while i < len(fields):
            comparator = comparators[0].upper()
            if i < len(comparators): comparator = comparators[i].upper()
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


    def to_list(self, rows):
        return [VideoTip(row["title"], row["url"], row["id"], bool(row["read"]))
                for row in rows]
