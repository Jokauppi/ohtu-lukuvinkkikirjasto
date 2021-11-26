from database_connection import get_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS BookTips;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE BookTips (
            name TEXT,
            author TEXT,
            isbn TEXT,
            publication_year INTEGER
        );
    """)

    connection.commit()


def initialise_database():
    connection = get_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialise_database()
