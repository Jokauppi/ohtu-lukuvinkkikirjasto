from ui.loopbreak import LoopBreak
from lukuvinkkikirjasto.ui.add_ui.add_ui import AddUI
from lukuvinkkikirjasto.ui.list_ui.print_ui import PrintUI
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
        self.print_ui = PrintUI(textio, self.menu, service, self.filter)
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
                "action": self.print_ui.print_tips,
                "message": "Tarkastele vinkkejä",
                "shortcut": "p"
            },
            
            {
                "action": self.set_filters,
                "message": "Aseta tai muokkaa suodattimia",
                "shortcut": "f"
            },
            {
                "action": self.tip_ui.choose_tip,
                "message": "Muokkaa vinkkiä",
                "shortcut": "c"
            },
#            {
#                "action": self.read_ui.print_tips,
#                "message": "Merkitse vinkki luetuksi",
#                "shortcut": "r"
#            },
#            {
#                "action": self.search_start,
#                "message": "Etsi vinkkejä",
#                "shortcut": "s"
#            },
#            {
#                "action": self.browser.run,
#                "message": "Selaa vinkkejä",
#                "shortcut": "b"
#            },
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

    def search_all_tips(self):
        tips = self.search_books()
        tips += self.search_blogs()
        tips += self.search_videos()
        return tips
    
    def search_books(self):
        f, v, c, sv, so = self.filter.book_filters()
        return self.service.search_book_tips(f, v, c, sv, so)

    def search_videos(self):
        f, v, c, sv, so = self.filter.video_filters()
        return self.service.search_video_tips(f, v, c, sv, so)

    def search_blogs(self):
        f, v, c, sv, so = self.filter.blog_filters()
        return self.service.search_blog_tips(f, v, c, sv, so)
