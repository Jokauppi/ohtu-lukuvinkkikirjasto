
class ListUI():
    def __init__(self, textio, menu, service, filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = filter

    def list_tips(self):
        tips = self.service.filter_tips(self.filter)

        if len(tips) == 0:
            self.textio.output("Ei vinkkejä")
        for item in tips:
            self.textio.output(item)

    def list_books(self):
        if len(self.service.get_all_book_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for book in self.service.get_all_book_tips():
            self.textio.output(book)

    def list_blogs(self):
        if len(self.service.get_all_blog_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for blog in self.service.get_all_blog_tips():
            self.textio.output(blog)

    def list_videos(self):
        if len(self.service.get_all_video_tips()) == 0:
            self.textio.output("Ei vinkkejä")
        for video in self.service.get_all_video_tips():
            self.textio.output(video)

    def list_read(self, read=True):
        result = self.service.get_read_book_tips(read) \
            + self.service.get_read_blog_tips(read) \
            + self.service.get_read_video_tips(read)

        if len(result) == 0:
            self.textio.output("Ei vinkkejä")
        for item in result:
            self.textio.output(item)

    def list_unread(self):
        self.print_read(False)
