from sqlite3.dbapi2 import Error
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
                "shortcut": "t"
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

    def show(self, tip):
        if isinstance(tip, BookTip):
            self.menu.show(self.actions_book, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, BlogTip):
            self.menu.show(self.actions_blog, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, VideoTip):
            self.menu.show(self.actions_video, "Valitse muokattava kenttä")(tip)

    def modify(self, tip, field, new):
        try:
            setattr(tip, field, new)
        except (TypeError, ValueError) as err:
            self.textio.output(err)
        self.service.modify(tip)

    def modify_name(self, tip):
        self.modify(tip, "name", self.textio.input("Title: "))

    def modify_author(self, tip):
        self.modify(tip, "author", self.textio.input("Author: "))

    def modify_isbn(self, tip):
        self.modify(tip, "isbn", self.textio.input("ISBN: "))

    def modify_year(self, tip):
        self.modify(tip, "publication_year", self.textio.input("Publication year: "))

    def modify_comment(self, tip):
        self.modify(tip, "comment", self.textio.input("Comment: "))

    def modify_url(self, tip):
        self.modify(tip, "url", self.textio.input("Url: "))

    def modify_title(self, tip):
        self.modify(tip, "title", self.textio.input("Title: "))
