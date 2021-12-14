import os

from ui.loopbreak import LoopBreak
from ui.add_ui.add_ui import AddUI
from ui.list_ui.list_ui import ListUI
from ui.filter_ui.filter_ui import FilterUI
from ui.tip_ui.tip_ui import TipUI
from entities.filter import Filter

if os.name == "nt" or os.getenv("TEXTMODE", 'False').lower() in ('true', '1', 't'):
    from ui.menu.text_menu import TextMenu as Menu # pylint: disable=ungrouped-imports
else:
    from ui.menu.console_menu import ConsoleMenu as Menu # pylint: disable=ungrouped-imports

class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.menu = Menu(self.textio)
        self.service = service

        self.filter = Filter()
        self.add_ui = AddUI(textio, self.menu, service)
        self.list_ui = ListUI(textio, self.menu, service, self.filter)
        self.filter_ui = FilterUI(textio, self.menu, service, self.filter)
        self.tip_ui = TipUI(textio, self.menu, service, self.list_ui)

    def run(self):

        commands = [
            {
                "action": self.add_ui.view,
                "message": "Lisää vinkki",
                "shortcut": "a"
            },
            {
                "action": self.list_ui.view,
                "message": "Tarkastele vinkkejä",
                "shortcut": "p"
            },

            {
                "action": self.filter_ui.view,
                "message": "Muokkaa suodattimia",
                "shortcut": "f"
            },
            {
                "action": self.tip_ui.view,
                "message": "Vinkin toiminnot",
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
