import sqlite3
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
                comment TEXT,
                tags TEXT,
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

        cursor.execute("""
            INSERT INTO BookTips (name, author, isbn, publication_year, comment, tags, read) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (book_tip.name, book_tip.author, book_tip.isbn,
              book_tip.publication_year, book_tip.comment, book_tip.tags, book_tip.read))

        self._connection.commit()


    def comment(self, book_tip, comment):
        cursor = self._connection.cursor()

        try:
            cursor.execute("UPDATE BookTips SET comment=? WHERE id = ?",
                            (comment,
                            book_tip.id_number))
            self._connection.commit()
            return True

        except sqlite3.Error as err:
            print(err)
            return False

    def update_tags(self, book_tip):
        cursor = self._connection.cursor()

        try:
            cursor.execute("UPDATE BookTips SET tags=? WHERE id = ?",
                            (book_tip.tags,
                            book_tip.id_number))
            self._connection.commit()
            return True

        except sqlite3.Error as err:
            print(err)
            return False

    def modify(self, modified_tip):
        cursor = self._connection.cursor()

        try:
            cursor.execute("""
                UPDATE BookTips SET name=?, author=?, isbn=?, publication_year=?, comment=?, tags=? WHERE id = ?
            """, (modified_tip.name, modified_tip.author, modified_tip.isbn,
                  modified_tip.publication_year, modified_tip.comment,
                  modified_tip.tags, modified_tip.id_number))
            self._connection.commit()
            return True

        except sqlite3.Error as err:
            print(err)
            return False


    def remove_row(self, book_tip):
        cursor = self._connection.cursor()

        cursor.execute(
            """DELETE FROM BookTips
                WHERE name = ? and author = ? and isbn = ? and publication_year = ? and read = ?""",
                       (book_tip.name, book_tip.author, book_tip.isbn,
                        book_tip.publication_year, book_tip.read))

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips")

        rows = cursor.fetchall()

        return self.to_list(rows)

    def get_read(self, read):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BookTips WHERE read=?", (read,))

        rows = cursor.fetchall()

        return self.to_list(rows)

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

    def mark_as_read(self, booktip):
        cursor = self._connection.cursor()
        if not isinstance(booktip, BookTip):
            raise TypeError("Wrong object type")
        if not booktip.id_number:
            return False
        try:
            cursor.execute("UPDATE BookTips SET read = 1 WHERE id = ?", (str(booktip.id_number)))
            self._connection.commit()
            return True
        except sqlite3.Error as err:
            print(err)
            return False

    def search_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        if not fields:
            return self.get_all()

        values = [x.lower() for x in values]

        if not sort_by_values:
            sort_by_values.append(fields[0])

        if not comparators:
            comparators.append('=')

        if not sort_by_orders:
            sort_by_orders.append('ASC')

        search_string = "SELECT * FROM BookTips "
        search_string += self.where_string(fields, comparators)
        search_string += self.order_string(sort_by_values, sort_by_orders)+";"

        k=0
        while k < len(comparators):
            if comparators[k].upper().strip()=='LIKE':
                values[k] = "%" + values[k] + "%"
            k += 1

        cursor = self._connection.cursor()

        cursor.execute(search_string, values)

        rows = cursor.fetchall()

        return self.to_list(rows)

    def where_string(self, fields, comparators):
        if not fields:
            return ""

        where_string = "WHERE lower(" + fields[0].lower() + ")" + comparators[0].upper() + "?"

        i=1
        while i < len(fields):
            comparator = comparators[0].upper()

            if i < len(comparators):
                comparator = comparators[i].upper()

            where_string +=  " AND lower("+ fields[i].lower() + ")" + comparator.upper() + "?"
            i += 1

        return where_string

    def order_string(self, sort_by_values, sort_by_orders):
        if not sort_by_values:
            return ""

        order_string = " ORDER BY " + sort_by_values[0].lower() + " " + sort_by_orders[0].upper()

        j=1
        while j < len(sort_by_values):
            order_string += ", " + sort_by_values[j].lower() + " " + sort_by_orders[j].upper()
            j += 1

        return order_string

    def to_list(self, rows):
        return [BookTip(
                row["name"],
                row["author"],
                row["isbn"],
                str(row["publication_year"]),
                row["comment"],
                row["id"],
                bool(row["read"]), # olio vaatii stringia, tietokannassa integer
                row["tags"]
            )
            for row in rows]
