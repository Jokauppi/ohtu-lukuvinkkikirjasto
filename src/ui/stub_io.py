class StubIO():
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def add_input(self, value:str):
        self.inputs.append(value)

    def input(self, query:str):
        if len(self.inputs) > 0:
            self.output(query)
            return self.inputs.pop(0)
        return ""

    def output(self, message):
        self.outputs.append(str(message))
