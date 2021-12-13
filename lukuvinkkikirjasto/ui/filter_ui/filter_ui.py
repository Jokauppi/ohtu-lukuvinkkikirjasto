from simple_term_menu import TerminalMenu
import os

class FilterUI:
    def __init__(self, textio, menu, service, filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = filter
    
    def view(self):
        while True:

            commands = [
                {
                    "action": "type",
                    "message": self.menu_string("Vinkin tyyppi", self.filter.types),
                    "shortcut": "t"
                },
                {
                    "action": "name",
                    "message": self.menu_string("Nimi/otsikko", self.filter.name),
                    "shortcut": "n"
                },
                {
                    "action": "author",
                    "message": self.menu_string("Kirjoittaja", self.filter.author),
                    "shortcut": "w"
                },
                {
                    "action": "isbn",
                    "message": self.menu_string("ISBN", self.filter.isbn),
                    "shortcut": "i"
                },
                {
                    "action": "publication_year",
                    "message": self.menu_string("Julkaisuvuosi", self.filter.publication_year),
                    "shortcut": "y"
                },
                {
                    "action": "url",
                    "message": self.menu_string("URL", self.filter.url),
                    "shortcut": "u"
                },
                {
                    "action": "read",
                    "message": self.menu_string("Luettu (k/e)", self.filter.read),
                    "shortcut": "r"
                },
                {
                    "action": self.filter.clear_filters,
                    "message": "Nollaa kaikki",
                    "shortcut": "c"
                },
                {
                    "action": "save",
                    "message": "Tallenna",
                    "shortcut": "s"
                }
            ]

            response = self.menu.show(commands, "Valitse muokattava suodatuskriteeri", cancel=False)

            if response == "save":
                break
            elif response == "type":
                self.set_types()
            elif type(response) == str:
                self.set_filter(response)
            else:
                response()

    def set_filter(self, attribute):
        while True:
            new_filter = self.textio.input("Syötä uusi arvo:")
            try:
                setattr(self.filter, attribute, new_filter)
                break
            except:
                self.textio.output("Virheellinen arvo")

    def menu_string(self, text, value):
        if value != "":
            return f"{text}: {value}"
        return f"{text}"

    def set_types(self):
        
        types = ["book", "blog", "video"]

        if os.name == "nt" or os.getenv("TEXTMODE", 'False').lower() in ('true', '1', 't'):
            self.textio.output("Syödä näytettävät tyypit pilkulla erotettuna")
            self.textio.output("Vaihtoehdot book, blog ja video")
            while True:
                try:
                    chosen = self.textio.input("Syötä tyypit: ")
                    chosen.replace(" ", "")
                    chosen = chosen.split(",")
                    self.filter.types = chosen
                    break
                except ValueError as err:
                    print(err)
        else:
            terminal_menu = TerminalMenu(
                types,
                multi_select=True,
                show_multi_select_hint=True,
                multi_select_empty_ok=True,
                multi_select_select_on_accept=False,
                preselected_entries=self.filter.types
            )
            menu_entry_indices = terminal_menu.show()
            chosen = types
            if terminal_menu.chosen_menu_entries:
                chosen = list(terminal_menu.chosen_menu_entries)
            self.filter.types = chosen
