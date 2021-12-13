from ui.modify_ui.modify_ui import ModifyUI
from ui.tag_ui.tag_ui import TagUI
from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip

class TipUI:
    def __init__(self, textio, menu, service, list_ui):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.list_ui = list_ui
        self.modify_ui = ModifyUI(textio, menu, service)
        self.tag_ui = TagUI(textio, menu, service)

        self.actions_book = [
            {
                "action": self.modify_name,
                "message": "Muokkaa Title",
                "shortcut": "t"
            },
            {
                "action": self.modify_author,
                "message": "Muokkaa Author",
                "shortcut": "a"
            },
            {
                "action": self.modify_isbn,
                "message": "Muokkaa ISBN",
                "shortcut": "i"
            },
            {
                "action": self.modify_year,
                "message": "Muokkaa Publication year",
                "shortcut": "p"
            },
            {
                "action": self.modify_comment,
                "message": "Muokkaa Comment",
                "shortcut": "m"
            }

        ]

        self.actions_blog = [
            {
                "action": self.modify_name,
                "message": "Muokkaa Title",
                "shortcut": "t"
            },
            {
                "action": self.modify_author,
                "message": "Muokkaa Author",
                "shortcut": "a"
            },
            {
                "action": self.modify_url,
                "message": "Muokkaa Url",
                "shortcut": "u"
            },
            {
                "action": self.modify_comment,
                "message": "Muokkaa Comment",
                "shortcut": "m"
            }
        ]

        self.actions_video = [
            {
                "action": self.modify_title,
                "message": "Muokkaa Title",
                "shortcut": "t"
            },
            {
                "action": self.modify_url,
                "message": "Muokkaa Url",
                "shortcut": "u"
            },
            {
                "action": self.modify_comment,
                "message": "Muokkaa Comment",
                "shortcut": "m"
            }
        ]


        self.actions = [
            {
                "action": self.service.mark_as_read,
                "message": "Merkitse vinkki luetuksi",
                "shortcut": "r"
            },
            {
                "action": self.modify_ui.choose_action,
                "message": "Muokkaa kenttiä",
                "shortcut": "m"
            },
            {
                "action": self.service.remove_tip,
                "message": "Poista vinkki",
                "shortcut": "d"
            },
            {
                "action": self.comment_tip,
                "message": "Kommentoi vinkkiä",
                "shortcut": "c"
            },
            {
                "action": self.tag_ui.show,
                "message": "Lisää tageja",
                "shortcut": "t"
            }
        ]

    def view(self):
        tip = self.choose_tip()
        self.choose_action(tip)

    def choose_tip(self):
        tips = self.service.filter_tips(self.list_ui.filter)
        self.list_ui.list_tips(tips, indexes=True)
        while True:
            try:
                index = self.textio.input("Valitse vinkin numero:")
                return tips[int(index)]
            except:
                self.textio.output("Virheellinen vinkin numero")

    def choose_action(self, tip):
        if isinstance(tip, BookTip):
            self.menu.show(self.actions + self.actions_book, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, BlogTip):
            self.menu.show(self.actions + self.actions_blog, "Valitse muokattava kenttä")(tip)
        if isinstance(tip, VideoTip):
            self.menu.show(self.actions + self.actions_video, "Valitse muokattava kenttä")(tip)

    def comment_tip(self, tip):
        comment = self.textio.input("Input comment:")
        self.service.comment(tip, comment)

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

