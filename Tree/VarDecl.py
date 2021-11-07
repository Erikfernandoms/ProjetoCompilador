class VarDecl():
    def __init__(self, type, token):
        self.type = type
        self.token = token
        self.value = token.value
        