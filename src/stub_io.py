class StubIO():
    def __init__(self, inputs=[]):
        self.inputs = inputs
        self.outputs = []

    def add_input(self, value:str):
            self.inputs.append(value)

    def input(self, query:str):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def output(self, message):
        self.outputs.append(message)
