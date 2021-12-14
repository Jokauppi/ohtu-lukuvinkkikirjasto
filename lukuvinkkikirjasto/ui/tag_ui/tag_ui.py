
class TagUI():
    def __init__(self, textio, menu, service):
        self.textio = textio
        self.service = service
        self.menu = menu

        self.actions = [
            {
                "action": self.add_tag,
                "message": "Lisää tag",
                "shortcut": "a"
            },
            {
                "action": self.remove_tag,
                "message": "Poista tag",
                "shortcut": "r"
            }
        ]

    def show(self, tip):
        self.menu.show(self.actions, title="Valitse toiminto")(tip)

    def add_tag(self, tip):
        tip.add_tag(self.textio.input("Tag: "))
        self.service.update_tags(tip)

    def remove_tag(self, tip):
        tip.remove_tag(self.textio.input("Tag: "))
        self.service.update_tags(tip)
