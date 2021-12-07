import sys
from ui.app import App
from ui.text_io import TextIO
from service import Service
from repositories.book_tip_repository import BookTipRepository
from repositories.blog_tip_repository import BlogTipRepository
from repositories.video_tip_repository import VideoTipRepository


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        print("args:", args)

    service = Service(BookTipRepository(), BlogTipRepository(), VideoTipRepository())
    textio = TextIO()
    app = App(textio, service)
    app.run()

if __name__ == "__main__":
    main()
