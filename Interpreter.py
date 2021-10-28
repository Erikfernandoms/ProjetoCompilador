import Tokens

class Interpreter(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.getToken()

    def error(self):
        raise Exception("SINTAXE INVALIDA")
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.getToken()
        else:
            self.error()   
         
    def Op(self):
        
        
    def VarAtrib(self):
        result = self.atributionTypes()
        while self.current_token.type in (Tokens.IDENTIFIER, Tokens.EQUAL, Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.IDENTIFIER:
                self.eat(Tokens.IDENTIFIER)
                result += " " + token.value
            elif token.type == Tokens.EQUAL:
                self.eat(Tokens.EQUAL)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.ENDEXPRESSION:
                self.eat(Tokens.ENDEXPRESSION)
                result += " " + token.value
        return result

    def VarDecl(self):
        result = self.types()
        while self.current_token.type in (Tokens.IDENTIFIER, Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.IDENTIFIER:
                self.eat(Tokens.IDENTIFIER)
                result += " " + token.value
            elif token.type == Tokens.ENDEXPRESSION:
                self.eat(Tokens.ENDEXPRESSION)
                result += " " + token.value
            
        return result

    def types(self):
        result = ""
        while self.current_token.type in (Tokens.STR, Tokens.INT, Tokens.FLT, Tokens.BOOLEAN):
            token = self.current_token
            if token.type == Tokens.STR:
                self.eat(Tokens.STR)
                result = token.value
            elif token.type == Tokens.INT:
                self.eat(Tokens.INT)
                result = token.value
            elif token.type == Tokens.FLT:
                self.eat(Tokens.FLT)
                result = token.value
            elif token.type == Tokens.BOOLEAN:
                self.eat(Tokens.BOOLEAN)
                result = token.value
        return result

    def atributionTypes(self):
        result = ""
        while self.current_token.type in (Tokens.STRING, Tokens.INTEGER, Tokens.FLOAT, Tokens.BOOLEANTRUE, Tokens.BOOLEANFALSE):
            token = self.current_token
            if token.type == Tokens.STRING:
                self.eat(Tokens.STRING)
                result = token.value
            elif token.type == Tokens.INTEGER:
                self.eat(Tokens.INTEGER)
                result = token.value
            elif token.type == Tokens.FLOAT:
                self.eat(Tokens.FLOAT)
                result = token.value
            elif token.type == Tokens.BOOLEANTRUE:
                self.eat(Tokens.BOOLEANTRUE)
                result = token.value
            elif token.type == Tokens.BOOLEANFALSE:
                self.eat(Tokens.BOOLEANFALSE)
                result = token.value
        return result

def open_arq(arq):
        file = open(arq)
        word = file.read()
        return word

def main():
    lexer = Tokens.Lexer(open_arq("teste.txt"))
    interpreter = Interpreter(lexer)
    result = interpreter.VarAtrib()
    print(result)
    
if __name__ == "__main__":
  main()