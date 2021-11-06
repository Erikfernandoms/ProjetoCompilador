class Interpreter(object):
    def __init__(self, parser):
        self.parser = parser

    def interpreter(self):
        tree = self.parser.parse()
        return tree
