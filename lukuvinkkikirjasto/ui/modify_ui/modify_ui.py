from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip

class ModifyUI():
    def __init__(self, textio, menu, service):
        self.textio = textio
        self.service = service
        self.menu = menu
        
        self.actions_book = [
            {
                "action": self.modify_name,
                "message": "Title",
                "shortcut": "t"
            },
            {
                "action": self.modify_author,
                "message": "Author",
                "shortcut": "a"
            },
            {
                "action": self.modify_isbn,
                "message": "ISBN",
                "shortcut": "i"
            },
            {
                "action": self.modify_year,
                "message": "Publication year",
                "shortcut": "p"
            },
            {
                "action": self.modify_comment,
                "message": "Comment",
                "shortcut": "c"
            }
        ]

        self.actions_blog = [
            {
                "action": self.modify_name,
                "message": "Title",
                "shortcut": "n"
            },
            {
                "action": self.modify_author,
                "message": "Author",
                "shortcut": "a"
            },
            {
                "action": self.modify_url,
                "message": "Url",
                "shortcut": "u"
            },
            {
                "action": self.modify_comment,
                "message": "Comment",
                "shortcut": "c"
            }
        ]

        self.actions_video = [
            {
                "action": self.modify_title,
                "message": "Title",
                "shortcut": "t"
            },
            {
                "action": self.modify_url,
                "message": "Url",
                "shortcut": "u"
            },
            {
                "action": self.modify_comment,
                "message": "Comment",
                "shortcut": "c"
            }
        ]

    def choose_action(self, tip):
        if isinstance(tip, BookTip):
            self.menu.show(self.actions_book, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, BlogTip):
            self.menu.show(self.actions_blog, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, VideoTip):
            self.menu.show(self.actions_video, "Valitse muokattava kenttä")(tip)

    def modify_name(self, tip):
        new = self.textio.input("Title: ")
        tip.name = new
        self.service.modify(tip)

    def modify_author(self, tip):
        new = self.textio.input("Author: ")
        tip.author = new
        self.service.modify(tip)

    def modify_isbn(self, tip):
        new = self.textio.input("ISBN: ")
        tip.isbn = new
        self.service.modify(tip)

    def modify_year(self, tip):
        new = self.textio.input("Publication year: ")
        tip.publication_year = new
        self.service.modify(tip)

    def modify_comment(self, tip):
        new = self.textio.input("Comment: ")
        tip.comment = new
        self.service.modify(tip)

    def modify_url(self, tip):
        new = self.textio.input("Url: ")
        tip.url = new
        self.service.modify(tip)

    def modify_title(self, tip):
        new = self.textio.input("Title: ")
        tip.title = new
        self.service.modify(tip)
