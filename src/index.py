import sys
from app import App
from text_io import TextIO
from service import Service
from repositories.book_tip_repository import BookTipRepository
from database_connection import get_connection

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        print("args:", args)

    service = Service(BookTipRepository(get_connection()))
    io = TextIO()
    app = App(io, service)
    app.run()

if __name__ == "__main__":
    main()
