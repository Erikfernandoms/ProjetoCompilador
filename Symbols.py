class Symbols:
    instance: "Symbols"

    def __init__(self, name:str, type:str) -> None:
        self.name = name
        self.type = type
        
    def format(self):
        return f'[{self.name}:{self.type}]'