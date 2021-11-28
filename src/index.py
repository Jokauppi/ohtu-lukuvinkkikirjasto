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

    service = Service(BookTipRepository())
    textio = TextIO()
    app = App(textio, service)
    app.run()

if __name__ == "__main__":
    main()
