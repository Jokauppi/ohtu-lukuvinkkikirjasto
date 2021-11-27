from app import App
from stub_io import StubIO
from service import Service
from repositories.book_tip_repository import BookTipRepository
from database_test_connection import get_connection

class AppLibrary:
    def __init__(self):
        self._db = "acceptance.db"
        self._io = None
        self._app = None
        self.setup_service()

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def setup_service(self):
        self._io = StubIO()
        repository = BookTipRepository(get_connection(self._db))
        service = Service(repository)

        self._app = App(
            self._io,
            service
        )

    def run_application(self):
        self._app.run()
