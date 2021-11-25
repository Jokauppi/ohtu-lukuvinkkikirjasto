from database_connection import get_connection


def drop_tables(connection):
    c = connection.cursor()

    c.execute("""
        DROP TABLE IF EXISTS books;
    """)

    connection.commit()


def create_tables(connection):
    c = connection.cursor()

    c.execute("""
        CREATE TABLE books (
            title TEXT,
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
