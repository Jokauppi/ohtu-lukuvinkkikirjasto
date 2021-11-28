from loopbreak import LoopBreak


class App():
    def __init__(self, io, service):
        self.io = io
        self.service = service

    def run(self):
        self.io.output("Tervetuloa vinkkisovellukseen! Kirjoita \"q\" poistuaksesi sovelluksesta")
        command_dict = {"q": self.quit_program,
                        "l": self.add_book,
                        "p": self.print_books}
        while True:
            answer = self.io.input("Mikä on komentosi?\n")
            action = command_dict.get(answer)
            if action is None:
                print("Virheellinen komento")
                continue
            try:
                action()
            except LoopBreak:
                break


    def quit_program(self):
        raise LoopBreak

    def add_book(self):
        name = self.io.input("Syötä kirjan nimi:\n")
        author = self.io.input("Syötä kirjailijan nimi:\n")
        isbn = self.io.input("Syötä kirjan ISBN-koodi:\n")
        publication_year = self.io.input("Syötä kirjan julkaisuvuosi:\n")
        
        self.service.create_book_tip(name, author, isbn, publication_year)
        self.io.output("Kirja lisätty")

    def print_books(self):
        for book in self.service.get_all_book_tips():
            print(book, "\n")
