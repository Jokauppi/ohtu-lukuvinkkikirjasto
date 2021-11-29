import sys
from ui.app import App
from ui.text_io import TextIO
from service import Service
from repositories.book_tip_repository import BookTipRepository

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
