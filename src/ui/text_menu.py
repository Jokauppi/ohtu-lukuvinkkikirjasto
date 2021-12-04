from ui.text_io import TextIO

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

    options_strings = list(map(lambda c : get_option(c), options))
    max_option_length = max(map(lambda o : len(o), options_strings))

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
            return(action)
        except:
            text_io.output("Virheellinen komento")

def no_op():
    pass

def get_option(command):

    if command["shortcut"]:
        return f"[{command['shortcut']}] {command['message']}"
    return command["message"]
