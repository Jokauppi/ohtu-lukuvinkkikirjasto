from ui.menu.text_menu import TextMenu

class ReadUI():
    def __init__(self, textio, menu, service):
        self.textio = textio
        self.service = service
        self.menu = menu

        self.commands = [
            {
                "action": self.print_books,
                "message": "Kirjavinkit",
                "shortcut": "k"
            },
            {
                "action": self.print_blogs,
                "message": "Blogivinkit",
                "shortcut": "b"
            },
            {
                "action": self.print_videos,
                "message": "Videovinkit",
                "shortcut": "v"
            },
        ]

    def print_tips(self):
        self.menu.show(self.commands, "Valitse kategoria")()

    def print_books(self):
        books = self.service.get_read_book_tips(False)
        if not books:
            self.textio.output("Ei lukemattomia vinkkejä")
        else:
            self.mark_book_as_read(books)

    def mark_book_as_read(self, books):
        for index, book in enumerate(books):
            self.textio.output(f"ID number: {index}")
            self.textio.output(book)
        id_number = int(self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n"))
        selected_book = books[id_number]
        self.service.mark_as_read(selected_book)

    def print_blogs(self):
        blogs = self.service.get_read_blog_tips(False)
        if not blogs:
            self.textio.output("Ei lukemattomia vinkkejä")
        else:
            self.mark_blog_as_read(blogs)

    def mark_blog_as_read(self, blogs):
        for index, blog in enumerate(blogs):
            self.textio.output(f"ID number: {index}")
            self.textio.output(blog)
        id_number = int(self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n"))
        selected_blog = blogs[id_number]
        self.service.mark_as_read(selected_blog)


    def print_videos(self):
        videos = self.service.get_read_video_tips(False)
        if not videos:
            self.textio.output("Ei lukemattomia vinkkejä")
        else:
            self.mark_video_as_read(videos)

    def mark_video_as_read(self, videos):
        for index, video in enumerate(videos):
            self.textio.output(f"ID number: {index}")
            self.textio.output(video)
        id_number = int(self.textio.input("Syötä luetuksi merkattavan vinkin id numero\n"))
        selected_video = videos[id_number]
        self.service.mark_as_read(selected_video)
