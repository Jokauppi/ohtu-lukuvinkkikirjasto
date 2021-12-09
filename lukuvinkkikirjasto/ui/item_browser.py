from ui.loopbreak import LoopBreak
from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip

class ItemBrowser():
    def __init__(self, textio, service):
        self.textio = textio
        self.service = service
        self.refresh_items()
        self.spot = 1

    def run(self):
        self.print_instructions()
        command_dict = {"<" : self.prev_item,
                        ">" : self.next_item,
                        "m" : self.modify,
                        "b" : self.quit_browser,
                        "d" : self.delete_item}
        while True:
            if len(self.items) == 0:
                print("Ei vinkkejä")
                return
            self.show_tip()
            answer = self.textio.input("Mikä on komentosi?\n")
            action = command_dict.get(answer)
            if action is None:
                print("Virheellinen komento")
                self.print_instructions()
                continue
            try:
                action()
            except LoopBreak:
                self.textio.output("Palataan päävalikkoon")
                break

    def print_instructions(self):
        self.textio.output("<: edellinen vinkki")
        self.textio.output(">: seuraava vinkki")
        self.textio.output("b: palaa päävalikkoon")
        self.textio.output("d: poista vinkki\n")

    def prev_item(self):
        self.spot = max(1, self.spot-1)

    def next_item(self):
        self.spot = min(len(self.items), self.spot+1)

    def modify(self):
        pass

    def delete_item(self):
        item = self.items[self.spot-1]
        if isinstance(item, BookTip):
            self.service.remove_book_tip(self.items[self.spot-1])
        elif isinstance(item, BlogTip):
            self.service.remove_blog_tip(self.items[self.spot-1])
        elif isinstance(item, VideoTip):
            self.service.remove_video_tip(self.items[self.spot-1])
        self.refresh_items()

    def refresh_items(self):
        self.items = self.service.get_all_book_tips() + self.service.get_all_blog_tips() + self.service.get_all_video_tips()

    def quit_browser(self):
        raise LoopBreak

    def show_tip(self):
        self.textio.output(self.items[self.spot-1])
