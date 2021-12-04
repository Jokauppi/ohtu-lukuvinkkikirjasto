from ui.loopbreak import LoopBreak
from ui.book_browser import BookBrowser
from ui.print_ui import PrintUI
from ui.add_ui import AddUI
from ui.console_menu import show_menu


class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service
        
        self.browser = BookBrowser(textio, service)
        self.print_ui = PrintUI(textio, service)
        self.add_ui = AddUI(textio, service)

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
                "action": self.mark_as_read,
                "message": "Merkitse vinkki luetuksi",
                "shortcut": "r"
            },
            {
                "action": self.search_start,
                "message": "Etsi vinkkejä",
                "shortcut": "s"
            },
            {
                "action": self.quit_program,
                "message": "Poistu sovelluksesta",
                "shortcut": "q"
            },
        ]

        while True:
            try:
                show_menu(commands, "Lukuvinkkikirjasto", cancel=False)["action"]()
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
        command_dict = {"n": self.search_name,
                        "t": self.search_creator,
                        "k": self.search_books,
                        "v": self.search_videos,
                        "b": self.search_blogs}
        
        action = None
        while action is None:        
                choice = self.textio.input("Etsi mitä? (N=nimi (teoksen), T=Tekijä, K=Kirja, V=Video, B=Blogi, L=Lopeta): ").lower()
                if (choice == 'l'): return
                action = command_dict.get(choice)

                if action is None:
                    print("Virheellinen komento\n")
                else:
                    results = action()
                    print("-------------\n")
                    print("Haku: " + str(len(results)) + " tulosta\n")
                    for result in results:
                        self.textio.output(result)



    def search_name(self):
        fields = []
        values = []
        sortByValues = []
        sortbyOrders = []
        comparators = []
        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'name', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'author', 'ASC')
        tips = self.service.search_tips(fields, values, comparators, sortByValues, sortbyOrders)
        return tips

    def search_creator(self):
        fields = []
        values = []
        sortByValues = []
        sortbyOrders = []
        comparators = []
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'author', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'name', 'ASC')
        tips = self.service.search_tips(fields, values, comparators, sortByValues, sortbyOrders)
        return tips

    
    def search_books(self):
        fields = []
        values = []
        sortByValues = []
        sortbyOrders = []
        comparators = []

        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        isbn = self.textio.input("ISBN (tai tyhjä): ")
        publication_year = self.textio.input("Julkaisuvuosi (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")

        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'name', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'author', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'publication_year', publication_year, '=')
        self.add_sortBys(sortByValues, sortbyOrders, 'publication_year', 'DESC')
        self.add_field_and_value(fields, values, comparators, 'isbn', isbn, '=')
        if isread.lower() == 'k': self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e': self.add_field_and_value(fields, values, comparators, 'read', '0', '=')


        tips = self.service.search_book_tips(fields, values, comparators, sortByValues, sortbyOrders)
        return tips



    
    def search_videos(self):
        return
    
    def search_blogs(self):
        fields = []
        values = []
        sortByValues = []
        sortbyOrders = []
        comparators = []

        name = self.textio.input("Teoksen nimi (tai tyhjä): ")
        author = self.textio.input("Tekijän nimi (tai tyhjä): ")
        url = self.textio.input("url (tai tyhjä): ")
        isread = self.textio.input("Merkitty luetuksi (K = Kyllä, E = Ei, Tyhjä = Ei väliä): ")

        self.add_field_and_value(fields, values, comparators, 'name', name, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'name', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'author', author, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'author', 'ASC')
        self.add_field_and_value(fields, values, comparators, 'url', url, ' LIKE ')
        self.add_sortBys(sortByValues, sortbyOrders, 'url', 'ASC')
        if isread.lower() == 'k': self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if isread.lower() == 'e': self.add_field_and_value(fields, values, comparators, 'read', '0', '=')

        tips = self.service.search_blog_tips(fields, values, comparators, sortByValues, sortbyOrders)
        return tips


        
    def add_field_and_value(self, fields, values, comparators, field, value, comparator='='):
        if value:
            fields.append(field)
            values.append(value)
            comparators.append(comparator)
    
    def add_sortBys(self, sortByValues, sortbyOrders, value, order='ASC'):
        if value:
            sortByValues.append(value)
            sortbyOrders.append(order)
