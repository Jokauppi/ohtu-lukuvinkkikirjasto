class FilterUI:
    def __init__(self, textio, menu, service, filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = filter

        self.commands = [
            {
                "action": filter.clear_filters,
                "message": "Nollaa kaikki",
                "shortcut": "c"
            },
            {
                "action": "save",
                "message": "Tallenna",
                "shortcut": "s"
            }
        ]
    
    def view(self):
        while True:
            response = self.menu.show(self.commands, "Valitse muokattava suodatin", cancel=False)

            if response == "save":
                break

            response()

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
