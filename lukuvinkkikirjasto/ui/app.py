from ui.loopbreak import LoopBreak
from ui.item_browser import ItemBrowser
from ui.print_ui import PrintUI
from ui.add_ui import AddUI
from ui.read_ui import ReadUI
from entities.filter import Filter

import os
if os.name == "nt" or os.getenv("TEXTMODE", 'False').lower() in ('true', '1', 't'):
    from ui.text_menu import TextMenu as Menu
else:
    from ui.console_menu import ConsoleMenu as Menu

class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.menu = Menu(self.textio)
        self.service = service

        self.browser = ItemBrowser(textio, service)
        self.print_ui = PrintUI(textio, self.menu, service)
        self.add_ui = AddUI(textio, self.menu, service)
        self.read_ui = ReadUI(textio, self.menu, service)
        self.filter = Filter()

    def run(self):

        commands = [
            {
                "action": self.add_ui.add_tip,
                "message": "Lisää vinkki",
                "shortcut": "a"
            },
            {
                "action": self.print_ui.print_tips,
                "message": "Tulosta vinkkejä",
                "shortcut": "p"
            },
            
            {
                "action": self.set_filters,
                "message": "Aseta tai muokkaa suodattimia",
                "shortcut": "f"
            },
            {
                "action": self.read_ui.print_tips,
                "message": "Merkitse vinkki luetuksi",
                "shortcut": "r"
            },
            {
                "action": self.search_start,
                "message": "Etsi vinkkejä",
                "shortcut": "s"
            },
            {
                "action": self.browser.run,
                "message": "Selaa vinkkejä",
                "shortcut": "b"
            },
            {
                "action": self.quit_program,
                "message": "Poistu sovelluksesta",
                "shortcut": "q"
            }
        ]

        while True:
            try:
                self.menu.show(commands, "Lukuvinkkikirjasto", cancel=False)()
            except LoopBreak:
                break

    def quit_program(self):
        raise LoopBreak

    def mark_as_read(self):
        for book in self.service.get_all_book_tips():
            self.textio.output(f"ID number: {book.id_number}")
            self.textio.output(f"Read: {book.read}")
            self.textio.output(book)
        id_number = self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n")
        self.service.mark_book_tip_as_read(id_number)

    def browse_books(self):
        self.browser.run()

    def set_filters(self):
        choice = "-1"
        while choice:
            self.textio.output(self.filter)
            choice = self.textio.input("Valitse muokattava filtteri (1, 2,... TYHJÄ = lopeta,  0 = Tyhjennä kaikki): ").lower()
            if not choice:
                self.textio.output("")
                return
            if choice == "0":
                self.filter.clear_filters()
            else:
                value = self.textio.input("Suodattimen " +choice+ " uusi arvo: ").lower()
                self.filter.set_choice(choice, value)

    def search_start(self):
        command_dict = {"k": self.search_books,
                        "v": self.search_videos,
                        "b": self.search_blogs}

        action = None
        while action is None:
            choice = self.textio.input("Etsi mitä? (Tyhjä = Kaikki tyypit, K = Kirja,"
                                       "V = Video, B = Blogi, L = Lopeta): ").lower()

            if choice == 'l':
                return
            action = command_dict.get(choice)

            if not choice:
                action = self.search_all_tips

            if action is None:
                self.textio.output("Virheellinen komento\n")
            else:
                results = action()
                self.textio.output("-------------\n")
                self.textio.output("Haku: " + str(len(results)) + " tulosta\n")
                for result in results:
                    self.textio.output(result)
