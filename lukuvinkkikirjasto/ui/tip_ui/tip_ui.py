class TipUI:
    def __init__(self, textio, menu, service, filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = filter

        self.commands = [
            {
                "action": lambda *args: None,
                "message": "Vinkki",
                "shortcut": "v"
            }
        ]

    def choose_tip(self):
        pass

