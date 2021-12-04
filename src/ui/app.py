from ui.loopbreak import LoopBreak
from ui.book_browser import BookBrowser

class App():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service
        self.browser = BookBrowser(textio, service)

    def run(self):
        self.textio.output("Tervetuloa vinkkisovellukseen!")
        self.print_instructions()

        command_dict = {"q": self.quit_program,
                        "a": self.add_book,
                        "b": self.add_blog,
                        "c": self.add_video,
                        "p": self.print_books,
                        "pp": self.print_blogs,
                        "ppp": self.print_videos,
                        "r": self.mark_as_read,
                        "s": self.search_start}

        while True:
            answer = self.textio.input("Mikä on komentosi?\n")
            action = command_dict.get(answer)
            if action is None:
                print("Virheellinen komento")
                self.print_instructions()
                continue
            try:
                action()
            except LoopBreak:
                break


    def print_instructions(self):
        self.textio.output("q: poistu sovelluksesta")
        self.textio.output("a: lisää kirjavinkki")
        self.textio.output("b: lisää blogivinkki")
        self.textio.output("c: lisää videovinkki")
        self.textio.output("p: tulosta kirjavinkit")
        self.textio.output("pp: tulosta blogivinkit")
        self.textio.output("ppp: tulosta videovinkit")
        self.textio.output("r: merkitse vinkki luetuksi")
        self.textio.output("s: etsi vinkkejä") 

    def quit_program(self):
        raise LoopBreak

    def add_book(self):
        name = self.textio.input("Syötä kirjan nimi:\n")
        author = self.textio.input("Syötä kirjailijan nimi:\n")
        isbn = self.textio.input("Syötä kirjan ISBN-koodi:\n")
        publication_year = self.textio.input("Syötä kirjan julkaisuvuosi:\n")
        try:
            self.service.create_book_tip(name, author, isbn, publication_year)
            self.textio.output("Kirja lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Kirjan lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Kirjan lisäys ei onnistunut")

    def add_blog(self):
        name = self.textio.input("Syötä blogin nimi:\n")
        author = self.textio.input("Syötä blogin tekijän nimi:\n")
        url = self.textio.input("Syötä blogin url:\n")
        try:
            self.service.create_blog_tip(name, author, url)
            self.textio.output("Blogi lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Blogin lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Blogin lisäys ei onnistunut")

    def add_video(self):
        title = self.textio.input("Syötä videon otsikko:\n")
        url = self.textio.input("Syötä videon url:\n")
        try:
            self.service.create_video_tip(title, url)
            self.textio.output("Video lisätty")
        except ValueError as value_error:
            self.textio.output(value_error)
            self.textio.output("Videon lisäys ei onnistunut")
        except TypeError as type_error:
            self.textio.output(type_error)
            self.textio.output("Videon lisäys ei onnistunut")

    def mark_as_read(self):
        for book in self.service.get_all_book_tips():
            self.textio.output(f"ID number: {book.id_number}")
            self.textio.output(f"Read: {book.read}")
            self.textio.output(book)
        id_number = self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n")
        self.service.mark_book_tip_as_read(id_number)

    def print_books(self):
        if len(self.service.get_all_book_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for book in self.service.get_all_book_tips():
            self.textio.output(book)

    def print_blogs(self):
        if len(self.service.get_all_blog_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for blog in self.service.get_all_blog_tips():
            self.textio.output(blog)

    def print_videos(self):
        if len(self.service.get_all_video_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for video in self.service.get_all_video_tips():
            self.textio.output(video)

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
