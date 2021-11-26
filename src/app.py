from loopbreak import LoopBreak
class App():
    def __init__(self, io, service):
        self.io = io
        self.service = service
    
    def run(self):
        self.io.output("Tervettuloa vinkkisovellukseen! Kirjoita \"q\" poistuaksesi sovelluksesta")
        command_dict = {"q": self.quit_program,
                        "l": self.add_book}
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
        ISBN = self.io.input("Syötä kirjan ISBN -koodi:\n")
        publication_year = self.io.input("Syötä kirjan julkaisuvuosi:\n")
        
        print("Kirja lisätty")
