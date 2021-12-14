from ui.modify_ui.modify_ui import ModifyUI
from ui.tag_ui.tag_ui import TagUI

class TipUI:
    def __init__(self, textio, menu, service, list_ui):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.list_ui = list_ui
        self.modify_ui = ModifyUI(textio, menu, service)
        self.tag_ui = TagUI(textio, menu, service)

        self.actions = [
            {
                "action": self.service.mark_as_read,
                "message": "Merkitse vinkki luetuksi",
                "shortcut": "r"
            },
            {
                "action": self.service.remove_tip,
                "message": "Poista vinkki",
                "shortcut": "d"
            },
            {
                "action": self.modify_ui.show,
                "message": "Muokkaa vinkkiä",
                "shortcut": "m"
            },
            {
                "action": self.comment_tip,
                "message": "Kommentoi vinkkiä",
                "shortcut": "c"
            },
            {
                "action": self.tag_ui.show,
                "message": "Muokkaa tageja",
                "shortcut": "t"
            }
        ]

    def view(self):
        tip = self.choose_tip()
        self.choose_action(tip)

    def choose_tip(self):
        tips = self.service.filter_tips(self.list_ui.filter)
        self.list_ui.list_tips(tips, indexes=True)
        while True:
            try:
                index = self.textio.input("Valitse vinkin numero:")
                return tips[int(index)]
            except (KeyError, IndexError):
                self.textio.output("Virheellinen vinkin numero")

    def choose_action(self, tip):
        self.menu.show(self.actions, "Valitse toiminto")(tip)

    def comment_tip(self, tip):
        comment = self.textio.input("Input comment:")
        self.service.comment(tip, comment)
