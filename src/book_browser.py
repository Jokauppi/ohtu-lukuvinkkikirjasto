class BookBrowser():
    def __init__(self, io, service):
        self.io = io
        self.service = service
        self.spot = 1

    def run(self):
        if len(self.service.get_all_book_tips()) == 0:
            print("Ei vinkkejä")
        self.io.output("Kirjoita \"<\" katsoaksesi edellistä kirjaa, \">\" katsoaksesi" +
              "toista kirjaa, tai \"b\" palataksesi päävalikkoon")
        command_dict = {"<" : prev_book,
                        ">" : next_book,
                        "m" : modify}
        self.io.loop(command_dict)

    def prev_book(self):
        pass

    def next_book(self):
        pass

    def modify(self):
        pass
