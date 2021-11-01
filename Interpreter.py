import re
from typing import List
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

    def Conditional(self):
        result = self.ReadStatement()
        while self.current_token.type in (Tokens.IF, Tokens.ESQPARENT, Tokens.DIRPARENT, Tokens.TWOPOINTS,Tokens.ELIF, Tokens.ELSE, Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.IF:
                self.eat(Tokens.IF)
                result += " " + token.value 
            elif token.type == Tokens.ESQPARENT:
                self.eat(Tokens.ESQPARENT)
                result += " " + token.value + " " + self.ReadStatement()
            elif token.type == Tokens.DIRPARENT:
                self.eat(Tokens.DIRPARENT)
                result += " " + token.value
            elif token.type == Tokens.TWOPOINTS:
                self.eat(Tokens.TWOPOINTS)
                result += " " + token.value + " " + self.ReadStatement()
            elif token.type == Tokens.ELIF:
                self.eat(Tokens.ELIF)
                result += " " + token.value
            elif token.type == Tokens.ELSE:
                self.eat(Tokens.ELSE)
                result += " " + token.value
            elif token.type == Tokens.ENDEXPRESSION:
                self.eat(Tokens.ENDEXPRESSION)
                result += " " + token.value
        return result

    def ReadStatement(self):
        lista = self.Statement()
        result = ""
        for i in range(len(lista)):
            if (lista[i] != ''):
                result += lista[i]
        return result
    
    def Statement(self) -> list:
        return self.VarDecl(), self.VarAtrib(), self.atributionTypes(), self.types(), self.RelOp(), self.Op(), self.Operators()

    def Operators(self):
        result = ""
        while self.current_token.type in (Tokens.NOT, Tokens.AND, Tokens.OR):
            token = self.current_token
            if token.type == Tokens.NOT:
                self.eat(Tokens.NOT)
                result += " " + token.value 
            elif token.type == Tokens.AND:
                self.eat(Tokens.AND)
                result += " " + token.value
            elif token.type == Tokens.OR:
                self.eat(Tokens.OR) 
                result += " " + token.value 
        return result

    def RelOp(self):
        result = self.atributionTypes() 
        while self.current_token.type in (Tokens.IDENTIFIER, Tokens.ENDEXPRESSION,Tokens.ESQMAIOR, Tokens.DIRMAIOR, Tokens.ESQME, Tokens.DIRME, Tokens.DIF, Tokens.EQUALCOMP):
            token = self.current_token
            if token.type == Tokens.IDENTIFIER:
                self.eat(Tokens.IDENTIFIER)
                result += " " + token.value 
            elif token.type == Tokens.ENDEXPRESSION:
                self.eat(Tokens.ENDEXPRESSION)
                result += " " + token.value
            elif token.type == Tokens.ESQMAIOR:
                self.eat(Tokens.ESQMAIOR) 
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.DIRMAIOR:
                self.eat(Tokens.DIRMAIOR)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.ESQME:
                self.eat(Tokens.ESQME)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.DIRME:
                self.eat(Tokens.DIRME)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.DIF:
                self.eat(Tokens.DIF)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.EQUAL:
                self.eat(Tokens.EQUALCOMP)
                result += " " + token.value + " " + self.atributionTypes()
        return result

    def Op(self):
        result= self.atributionTypes() 
        while self.current_token.type in (Tokens.IDENTIFIER, Tokens.ENDEXPRESSION,Tokens.SUM, Tokens.SUB, Tokens.MULT, Tokens.DIV, Tokens.POW, Tokens.SQRT):
            token = self.current_token
            if token.type == Tokens.IDENTIFIER:
                self.eat(Tokens.IDENTIFIER)
                result += " " + token.value 
            elif token.type == Tokens.ENDEXPRESSION:
                self.eat(Tokens.ENDEXPRESSION)
                result += " " + token.value
            elif token.type == Tokens.SUM:
                self.eat(Tokens.SUM) 
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.SUB:
                self.eat(Tokens.SUB)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.MULT:
                self.eat(Tokens.MULT)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.DIV:
                self.eat(Tokens.DIV)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.POW:
                self.eat(Tokens.POW)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.SQRT:
                self.eat(Tokens.SQRT)
                result += " " + token.value + " " + self.atributionTypes()
        return result
        
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
    result = interpreter.Conditional()
    print(result)
    
if __name__ == "__main__":
  main()