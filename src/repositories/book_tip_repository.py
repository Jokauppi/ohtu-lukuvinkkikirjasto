from entities.book_tip import BookTip
from repositories.database_connection import get_connection

class BookTipRepository:
    def __init__(self, connection=get_connection()):
        self._connection = connection
        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BookTips (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author TEXT,
                isbn TEXT,
                publication_year INTEGER,
                read INTEGER
            );
        """)

        connection.commit()

    def add(self, book_tip):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips WHERE isbn=?", (book_tip.isbn,))

        result = cursor.fetchone()

        if result:
            return

        cursor.execute("INSERT INTO BookTips (name, author, isbn, publication_year, read) VALUES (?, ?, ?, ?, ?)",
            (book_tip.name, book_tip.author, book_tip.isbn, book_tip.publication_year, 0))

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips")

        rows = cursor.fetchall()

        return [BookTip(row["name"], row["author"], row["isbn"], str(row["publication_year"]), row["id"], bool(row["read"]))
                 # olio vaatii stringia, tietokannassa integer
                for row in rows]

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from BookTips')

        self._connection.commit()

    def drop_tables(self):
        cursor = self._connection.cursor()

        cursor.execute("""
            DROP TABLE IF EXISTS BookTips;
        """)

        self._connection.commit()

    def mark_as_read(self, id_number):
        cursor = self._connection.cursor()
        try:
            cursor.execute("UPDATE BookTips SET read = 1 WHERE id = ?", (id_number))
            self._connection.commit()
            return True
        except:
            return False
    
    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders=['ASC']):
        if not fields: return []
        values = [x.lower() for x in values]
        if not sortByValues: sortByValues.append(fields[0])
        if not comparators: comparators.append('=')

        search_string = "SELECT * FROM BookTips WHERE lower(" + fields[0].lower() + ")" + comparators[0]+"?"
        
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

        return [BookTip(
            row["name"],
            row["author"],
            row["isbn"],
            str(row["publication_year"])) # olio vaatii stringia, tietokannassa integer
            for row in rows]


