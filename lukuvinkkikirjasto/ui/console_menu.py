from simple_term_menu import TerminalMenu

class ConsoleMenu:
    def __init__(self):
        pass
    def show(self, commands, title=None, cancel=True):

        options = commands.copy()

        if cancel:
            options.append({
                "action": self.no_op,
                "message": "Peruuta",
                "shortcut": None
            })

        options_strings = [self.get_option(c) for c in options]

        terminal_menu = TerminalMenu(options_strings, title=title)

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]["action"]

    def no_op(self):
        pass

    def get_option(self, command):

        if command["shortcut"]:
            return f"[{command['shortcut']}] {command['message']}"
        return command["message"]
