from ui.loopbreak import LoopBreak
from ui.book_browser import BookBrowser

class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service
        self.browser = BookBrowser(textio, service)

    def run(self):
        self.textio.output("Tervetuloa vinkkisovellukseen!")
        self.print_instructions()

        command_dict = {"q": self.quit_program,
                        "a": self.add_book,
                        "p": self.print_books,
                        "r": self.mark_as_read}

        while True:
            answer = self.textio.input("Mikä on komentosi?\n")
            action = command_dict.get(answer)
            if action is None:
                print("Virheellinen komento")
                self.print_instructions()
                continue
            try:
                action()
            except LoopBreak:
                break


    def print_instructions(self):
        self.textio.output("q: poistu sovelluksesta")
        self.textio.output("a: lisää kirjavinkki")
        self.textio.output("p: tulosta kirjavinkit")
        self.textio.output("r: merkitse vinkki luetuksi") 

    def quit_program(self):
        raise LoopBreak

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

    def mark_as_read(self):
        id_number = self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n")
        self.service.mark_book_tip_as_read(id_number)

    def print_books(self):
        if len(self.service.get_all_book_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for book in self.service.get_all_book_tips():
            self.textio.output(f"Index: {book['id']}")           #Väliaikainen tulostus
            self.textio.output(f"Read status: {book['read']}")   #Väliaikainen tulostus
            self.textio.output(book['item'])

    def browse_books(self):
        self.browser.run()
