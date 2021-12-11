from ui.loopbreak import LoopBreak
from lukuvinkkikirjasto.ui.add_ui.add_ui import AddUI
from lukuvinkkikirjasto.ui.list_ui.list_ui import ListUI
from lukuvinkkikirjasto.ui.filter_ui.filter_ui import FilterUI
from lukuvinkkikirjasto.ui.tip_ui.tip_ui import TipUI
from entities.filter import Filter

import os
if os.name == "nt" or os.getenv("TEXTMODE", 'False').lower() in ('true', '1', 't'):
    from ui.menu.text_menu import TextMenu as Menu
else:
    from ui.menu.console_menu import ConsoleMenu as Menu

class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.menu = Menu(self.textio)
        self.service = service

        self.filter = Filter()
        self.add_ui = AddUI(textio, self.menu, service)
        self.list_ui = ListUI(textio, self.menu, service, self.filter)
        self.filter_ui = FilterUI(textio, self.menu, service, self.filter)
        self.tip_ui = TipUI(textio, self.menu, service, self.filter)

    def run(self):

        commands = [
            {
                "action": self.add_ui.add_tip,
                "message": "Lisää vinkki",
                "shortcut": "a"
            },
            {
                "action": self.list_ui.list_tips,
                "message": "Tarkastele vinkkejä",
                "shortcut": "p"
            },
            
            {
                "action": self.filter_ui.view,
                "message": "Aseta tai muokkaa suodattimia",
                "shortcut": "f"
            },
            {
                "action": self.tip_ui.choose_tip,
                "message": "Muokkaa vinkkiä",
                "shortcut": "c"
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

