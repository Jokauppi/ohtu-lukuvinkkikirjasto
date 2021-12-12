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
                    "action": self.filter.types,
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
            
            if type(response) == str:
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
