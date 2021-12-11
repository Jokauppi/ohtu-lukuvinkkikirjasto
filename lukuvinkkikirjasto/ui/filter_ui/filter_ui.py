class FilterUI:
    def __init__(self, textio, menu, service, filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = filter

        self.commands = [
            {
                "action": lambda *args: None,
                "message": "filter",
                "shortcut": "f"
            }
        ]
