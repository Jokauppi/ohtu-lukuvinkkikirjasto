import sqlite3
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
            (video_tip.title, video_tip.url, video_tip.read))

        self._connection.commit()

    def remove_row(self, video_tip):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM VideoTips WHERE title = ? and url = ? and read = ?",
                       (video_tip.title, video_tip.url, video_tip.read))

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

    def mark_as_read(self, videotip):
        cursor = self._connection.cursor()
        if not isinstance(videotip, VideoTip):
            raise TypeError("Wrong object type")
        if not videotip.id_number:
            return False
        try:
            cursor.execute("UPDATE Videotips SET read = 1 WHERE id = ?", (str(videotip.id_number)))
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

        search_string = "SELECT * FROM Videotips "
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
        return [VideoTip(row["title"], row["url"], row["id"], bool(row["read"]))
                for row in rows]
