from loopbreak import LoopBreak

class TextIO():
    def __init__(self):
        pass

    def input(self, query:str):
        return str(input(query))

    def output(self, message):
        print(message)

    def loop(self, command_dict):
        while True:
            answer = self.input("Mikä on komentosi?\n")
            action = command_dict.get(answer)
            if action is None:
                print("Virheellinen komento")
                continue
            try:
                action()
            except LoopBreak:
                break
