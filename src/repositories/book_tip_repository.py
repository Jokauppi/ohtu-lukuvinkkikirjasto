from entities.book_tip import BookTip
from repositories.database_connection import get_connection

class BookTipRepository:
    def __init__(self, connection=get_connection()):
        self._connection = connection
        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BookTips (
                name TEXT,
                author TEXT,
                isbn TEXT,
                publication_year INTEGER
            );
        """)

        connection.commit()

    def add(self, book_tip):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips WHERE isbn=?", (book_tip.isbn,))

        result = cursor.fetchone()

        if result:
            return

        cursor.execute("INSERT INTO BookTips VALUES (?, ?, ?, ?)",
            (book_tip.name, book_tip.author, book_tip.isbn, book_tip.publication_year))

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips")

        rows = cursor.fetchall()

        return [BookTip(
            row["name"],
            row["author"],
            row["isbn"],
            str(row["publication_year"])) #Hakkeroit ratkaisu siihen, että olio vaatii stringiä mmutta tietokannassa on integer
            for row in rows]
    
    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from BookTips')

        self._connection.commit()

    def drop_tables(connection):
        cursor = connection.cursor()

        cursor.execute("""
            DROP TABLE IF EXISTS BookTips;
        """)

        connection.commit()
