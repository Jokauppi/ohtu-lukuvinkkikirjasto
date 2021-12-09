from ui.loopbreak import LoopBreak
from ui.item_browser import ItemBrowser
from ui.print_ui import PrintUI
from ui.add_ui import AddUI
from ui.read_ui import ReadUI
from ui.text_menu import TextMenu


class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service

        self.menu = TextMenu(self.textio)
        self.browser = ItemBrowser(textio, service)
        self.print_ui = PrintUI(textio, service)
        self.add_ui = AddUI(textio, service)
        self.read_ui = ReadUI(textio, service)

    def run(self):

        commands = [
            {
                "action": self.add_ui.add_tip,
                "message": "Lisää vinkki",
                "shortcut": "a"
            },
            {
                "action": self.print_ui.print_tips,
                "message": "Tulosta vinkkejä",
                "shortcut": "p"
            },
            {
                "action": self.read_ui.print_tips,
                "message": "Merkitse vinkki luetuksi",
                "shortcut": "r"
            },
            {
                "action": self.search_start,
                "message": "Etsi vinkkejä",
                "shortcut": "s"
            },
            {
                "action": self.browser.run,
                "message": "Selaa vinkkejä",
                "shortcut": "b"
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

    def mark_as_read(self):
        for book in self.service.get_all_book_tips():
            self.textio.output(f"ID number: {book.id_number}")
            self.textio.output(f"Read: {book.read}")
            self.textio.output(book)
        id_number = self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n")
        self.service.mark_book_tip_as_read(id_number)

    def browse_books(self):
        self.browser.run()

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
                print("Virheellinen komento\n")
            else:
                results = action()
                print("-------------\n")
                print("Haku: " + str(len(results)) + " tulosta\n")
                for result in results:
                    self.textio.output(result)

    def search_all_tips(self):
        fields = []
        values = []
        sort_by_values = []
        sort_by_orders = []
        comparators = []
        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")
        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'name', 'ASC')

        if isread.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')

        tips = self.service.search_book_tips \
            (fields, values, comparators, sort_by_values, sort_by_orders)
        tips += self.service.search_blog_tips \
            (fields, values, comparators, sort_by_values, sort_by_orders)

        if fields and fields[0] == 'name':
            fields[0]='title'
        if sort_by_values and sort_by_values[0] == 'name':
            sort_by_values[0]='title'

        for i in enumerate(fields):
            print(fields[i])
            print(sort_by_values[i])

        tips += self.service.search_video_tips \
            (fields, values, comparators, sort_by_values, sort_by_orders)

        return tips

    def search_books(self):
        fields = []
        values = []
        sort_by_values = []
        sort_by_orders = []
        comparators = []

        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        isbn = self.textio.input("ISBN (tai tyhjä): ")
        publication_year = self.textio.input("Julkaisuvuosi (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")

        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'name', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'author', 'ASC')
        self.add_field_and_value(fields,
                                values,
                                comparators,
                                'publication_year',
                                publication_year,
                                '=')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'publication_year', 'DESC')
        self.add_field_and_value(fields, values, comparators, 'isbn', isbn, '=')

        if isread.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')

        tips = self.service.search_book_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

        return tips

    def search_videos(self):
        fields = []
        values = []
        sort_by_values = []
        sort_by_orders = []
        comparators = []

        title = self.textio.input("Teoksen nimi (tai tyhjä): ")
        url = self.textio.input("url (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")

        self.add_field_and_value(fields, values, comparators, 'title', title, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'title', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'url', url, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'url', 'ASC')
        if isread.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')

        tips = self.service.search_video_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

        return tips

    def search_blogs(self):
        fields = []
        values = []
        sort_by_values = []
        sort_by_orders = []
        comparators = []

        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        url = self.textio.input("url (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")

        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'name', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'author', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'url', url, ' LIKE ')
        self.add_sort_bys(sort_by_values, sort_by_orders, 'url', 'ASC')

        if isread.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')

        tips = self.service.search_blog_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

        return tips

    def add_field_and_value(self, fields, values, comparators, field, value, comparator='='):
        if value:
            fields.append(field)
            values.append(value)
            comparators.append(comparator)

    def add_sort_bys(self, sort_by_values, sort_by_orders, value, order='ASC'):
        if value:
            sort_by_values.append(value)
            sort_by_orders.append(order)
