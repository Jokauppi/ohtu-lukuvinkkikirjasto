from simple_term_menu import TerminalMenu

def show_menu(commands, title=None, cancel=True):

    options = commands.copy()

    if cancel:
        options.append({
            "action": no_op,
            "message": "Peruuta",
            "shortcut": None
        })

    options_strings = [get_option(c) for c in options]

    terminal_menu = TerminalMenu(options_strings, title=title)

    menu_entry_index = terminal_menu.show()

    return options[menu_entry_index]["action"]

def no_op():
    pass

def get_option(command):

    if command["shortcut"]:
        return f"[{command['shortcut']}] {command['message']}"
    return command["message"]
