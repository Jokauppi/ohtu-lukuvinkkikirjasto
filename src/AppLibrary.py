from app import App
from entities.book_tip import BookTip
from stub_io import StubIO
from service import Service
from repositories.book_tip_repository import BookTipRepository
from repositories.database_connection import get_connection
import os

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

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def database_should_contain_book(self, name, author, isbn, publication):
        desired_book = BookTip(name, author, isbn, publication)
        all_books = self._service.get_all_book_tips()

        for book in all_books:
            if book == desired_book:
                break
        else:
            raise AssertionError("Desired book is not in database")

    def setup_app(self):
        self._io = StubIO()
        repository = BookTipRepository(get_connection(self._db))
        self._service = Service(repository)

        self._app = App(
            self._io,
            self._service
        )

    def clear_database(self):
        if os.path.exists(self._db):
            os.remove(self._db)

    def add_book_tip_to_service(self, name, author, isbn, publication):
        self._service.create_book_tip(name, author, isbn, publication)

    def run_application(self):
        self._app.run()
