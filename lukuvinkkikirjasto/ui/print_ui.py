
class PrintUI():
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
            {
                "action": self.print_read,
                "message": "Luetut",
                "shortcut": "r"
            },
            {
                "action": self.print_unread,
                "message": "Lukemattomat",
                "shortcut": "u"
            },
        ]

    def print_tips(self):
        self.menu.show(self.commands, "Valitse tulostettavat vinkit")()

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

    def print_read(self, read=True):
        result = self.service.get_read_book_tips(read) \
            + self.service.get_read_blog_tips(read) \
            + self.service.get_read_video_tips(read)

        if len(result) == 0:
            self.textio.output("Ei vinkkejä")
        for item in result:
            self.textio.output(item)

    def print_unread(self):
        self.print_read(False)
