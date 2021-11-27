from database_connection import get_connection
from entities.book_tip import BookTip


class BookTipRepository:
    def __init__(self, connection):
        self._connection = connection

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
            row["publication_year"])
            for row in rows]
