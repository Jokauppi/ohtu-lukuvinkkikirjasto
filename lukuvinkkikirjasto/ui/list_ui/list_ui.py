
class ListUI():
    def __init__(self, textio, menu, service, tip_filter):
        self.textio = textio
        self.service = service
        self.menu = menu
        self.filter = tip_filter

    def view(self):
        tips = self.service.filter_tips(self.filter)
        self.list_tips(tips)

    def list_tips(self, tips, indexes=False):

        if len(tips) == 0:
            self.textio.output("Ei vinkkejä")
        for index, item in enumerate(tips):
            self.textio.output("-"*15)
            if indexes:
                self.textio.output(f"[{index}]\n{item}")
            else:
                self.textio.output(item)
        self.textio.output("="*15)
