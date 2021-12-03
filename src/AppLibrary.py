import os
from entities.book_tip import BookTip
from entities.video_tip import VideoTip
from ui.app import App
from ui.stub_io import StubIO
from service import Service
from repositories.book_tip_repository import BookTipRepository
from repositories.blog_tip_repository import BlogTipRepository
from repositories.video_tip_repository import VideoTipRepository
from repositories.database_connection import get_connection

class AppLibrary:
    def __init__(self):
        self._db = os.getenv('ACCEPTANCE_DATABASE')
        self._io = None
        self._service = None
        self._app = None
        self.clear_database()
        self.setup_app()

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, desired):
        outputs = self._io.outputs

        for value in outputs:
            if str(desired) == str(value):
                break
        else:
            raise AssertionError(f"Output \"{desired}\" is not in\n{chr(10).join(outputs)}")

    def database_should_contain_book(self, name, author, isbn, publication):
        desired_book = BookTip(name, author, isbn, publication)
        all_books = self._service.get_all_book_tips()

        for book in all_books:
            if book == desired_book:
                break
        else:
            raise AssertionError("Desired book is not in database")

    def database_should_contain_video(self, title, url):
        desired_video = VideoTip(title, url)
        all_videos = self._service.get_all_video_tips()

        for video in all_videos:
            if video == desired_video:
                break
        else:
            raise AssertionError("Desired book is not in database")

    def setup_app(self):
        self._io = StubIO()
        book_repository = BookTipRepository(get_connection(self._db))
        blog_repository = BlogTipRepository(get_connection(self._db))
        video_repository = VideoTipRepository(get_connection(self._db))

        self._service = Service(book_repository, blog_repository, video_repository)

        self._app = App(
            self._io,
            self._service
        )

    def clear_database(self):
        if os.path.exists(self._db):
            try:
                os.remove(self._db)
            except OSError:
                pass

    def add_book_tip_to_service(self, name, author, isbn, publication):
        self._service.create_book_tip(name, author, isbn, publication)

    def run_application(self):
        self._app.run()
