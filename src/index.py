import sys
from app import App
from textio import Textio
from service import Service
from repositories.book_tip_repository import BookTipRepository
from database_connection import get_connection

class main():
    args = sys.argv[1:]
    if len(args) > 0:
        print("args:", args)

    service = Service(BookTipRepository(get_connection()))
    io = Textio()
    app = App(io, service)
    app.run()

if __name__ == "__main__":
    main()
