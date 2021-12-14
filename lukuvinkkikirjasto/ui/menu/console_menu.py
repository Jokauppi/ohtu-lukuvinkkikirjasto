from simple_term_menu import TerminalMenu

class ConsoleMenu:
    def __init__(self, text_io):
        pass

    def show(self, commands, title=None, cancel=True):

        options = commands.copy()

        if cancel:
            options.append({
                "action": self.no_op,
                "message": "Peruuta",
                "shortcut": "q"
            })

        options_strings = [self.get_option(c) for c in options]

        terminal_menu = TerminalMenu(options_strings, title=title, shortcut_key_highlight_style=("fg_cyan",))

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]["action"]

    def no_op(self, *args):
        pass

    def get_option(self, command):

        if command["shortcut"]:
            return f"[{command['shortcut']}] {command['message']}"
        return command["message"]
