from ui.text_menu import show_menu

class AddUI():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service

        self.commands = [
            {
                "action": self.add_book,
                "message": "Kirjavinkki",
                "shortcut": "k"
            },
            {
                "action": self.add_blog,
                "message": "Blogivinkki",
                "shortcut": "b"
            },
            {
                "action": self.add_video,
                "message": "Videovinkki",
                "shortcut": "v"
            }
        ]

    def add_tip(self):
        show_menu(self.commands, self.textio, "Valitse lisättävän vinkin tyyppi")()

    def add_book(self):
        name = self.textio.input("Syötä kirjan nimi:\n")
        author = self.textio.input("Syötä kirjailijan nimi:\n")
        isbn = self.textio.input("Syötä kirjan ISBN-koodi:\n")
        publication_year = self.textio.input("Syötä kirjan julkaisuvuosi:\n")
        try:
            self.service.create_book_tip(name, author, isbn, publication_year)
            self.textio.output("Kirja lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Kirjan lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Kirjan lisäys ei onnistunut")

    def add_blog(self):
        name = self.textio.input("Syötä blogin nimi:\n")
        author = self.textio.input("Syötä blogin tekijän nimi:\n")
        url = self.textio.input("Syötä blogin url:\n")
        try:
            self.service.create_blog_tip(name, author, url)
            self.textio.output("Blogi lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Blogin lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Blogin lisäys ei onnistunut")

    def add_video(self):
        title = self.textio.input("Syötä videon otsikko:\n")
        url = self.textio.input("Syötä videon url:\n")
        try:
            self.service.create_video_tip(title, url)
            self.textio.output("Video lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Videon lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Videon lisäys ei onnistunut")