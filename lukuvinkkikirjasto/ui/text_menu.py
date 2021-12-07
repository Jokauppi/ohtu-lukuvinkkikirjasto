def show_menu(commands, text_io, title=None, cancel=True):

    options = commands.copy()

    if cancel:
        options.append({
            "action": no_op,
            "message": "Peruuta",
            "shortcut": "q"
        })

    actions = {}
    for option in options:
        actions[option["shortcut"]] = option["action"]

    options_strings = [get_option(c) for c in options]
    max_option_length = len(max(options_strings, key=len))

    if title:
        text_io.output(title)

    text_io.output(max_option_length * "=")

    for opt_str in options_strings:
        text_io.output(opt_str)

    text_io.output(max_option_length * "=")

    while True:
        chosen = text_io.input("> ")
        try:
            action = actions[chosen]
            text_io.output("")
            return action
        except:
            text_io.output("Virheellinen komento")

def no_op():
    pass

def get_option(command):

    if command["shortcut"]:
        return f"[{command['shortcut']}] {command['message']}"
    return command["message"]
