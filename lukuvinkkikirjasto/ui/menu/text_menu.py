
class TextMenu:
    def __init__(self, text_io):
        self.text_io = text_io

    def show(self, commands, title=None, cancel=True):

        options = commands.copy()

        if cancel:
            options.append({
                "action": self.no_op,
                "message": "Peruuta",
                "shortcut": "q"
            })

        actions = {}
        for option in options:
            actions[option["shortcut"]] = option["action"]

        options_strings = [self.get_option(c) for c in options]
        max_option_length = len(max(options_strings, key=len))

        if title:
            self.text_io.output(title)

        self.text_io.output(max_option_length * "=")

        for opt_str in options_strings:
            self.text_io.output(opt_str)

        self.text_io.output(max_option_length * "=")

        while True:
            chosen = self.text_io.input("> ")
            try:
                action = actions[chosen]
                self.text_io.output("")
                return action
            except:
                self.text_io.output("Virheellinen komento")

    def no_op(self, *args):
        pass

    def get_option(self, command):

        if command["shortcut"]:
            return f"[{command['shortcut']}] {command['message']}"
        return command["message"]
