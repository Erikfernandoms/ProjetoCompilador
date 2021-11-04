import re
from typing import List
import Tokens.Tokens

class Parser(object):

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
        while self.current_token.type in (Tokens.Tokens.IF, Tokens.Tokens.ESQPARENT, Tokens.Tokens.DIRPARENT, Tokens.Tokens.TWOPOINTS,Tokens.Tokens.ELIF, Tokens.Tokens.ELSE, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IF:
                self.eat(Tokens.Tokens.IF)
                result += " " + token.value 
            elif token.type == Tokens.Tokens.ESQPARENT:
                self.eat(Tokens.Tokens.ESQPARENT)
                result += " " + token.value + " " + self.ReadStatement()
            elif token.type == Tokens.Tokens.DIRPARENT:
                self.eat(Tokens.Tokens.DIRPARENT)
                result += " " + token.value
            elif token.type == Tokens.Tokens.TWOPOINTS:
                self.eat(Tokens.Tokens.TWOPOINTS)
                result += " " + token.value + " " + self.ReadStatement()
            elif token.type == Tokens.Tokens.ELIF:
                self.eat(Tokens.Tokens.ELIF)
                result += " " + token.value
            elif token.type == Tokens.Tokens.ELSE:
                self.eat(Tokens.Tokens.ELSE)
                result += " " + token.value
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
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
        while self.current_token.type in (Tokens.Tokens.NOT, Tokens.Tokens.AND, Tokens.Tokens.OR):
            token = self.current_token
            if token.type == Tokens.Tokens.NOT:
                self.eat(Tokens.Tokens.NOT)
                result += " " + token.value 
            elif token.type == Tokens.Tokens.AND:
                self.eat(Tokens.Tokens.AND)
                result += " " + token.value
            elif token.type == Tokens.Tokens.OR:
                self.eat(Tokens.Tokens.OR) 
                result += " " + token.value 
        return result

    def RelOp(self):
        result = self.atributionTypes() 
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION,Tokens.Tokens.ESQMAIOR, Tokens.Tokens.DIRMAIOR, Tokens.Tokens.ESQME, Tokens.Tokens.DIRME, Tokens.Tokens.DIF, Tokens.Tokens.EQUALCOMP):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                result += " " + token.value 
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                result += " " + token.value
            elif token.type == Tokens.Tokens.ESQMAIOR:
                self.eat(Tokens.Tokens.ESQMAIOR) 
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.DIRMAIOR:
                self.eat(Tokens.Tokens.DIRMAIOR)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.ESQME:
                self.eat(Tokens.Tokens.ESQME)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.DIRME:
                self.eat(Tokens.Tokens.DIRME)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.DIF:
                self.eat(Tokens.Tokens.DIF)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.EQUAL:
                self.eat(Tokens.Tokens.EQUALCOMP)
                result += " " + token.value + " " + self.atributionTypes()
        return result

    def Op(self):
        result= self.atributionTypes() 
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION,Tokens.Tokens.SUM, Tokens.Tokens.SUB, Tokens.Tokens.MULT, Tokens.Tokens.DIV, Tokens.Tokens.POW, Tokens.Tokens.SQRT):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                result += " " + token.value 
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                result += " " + token.value
            elif token.type == Tokens.Tokens.SUM:
                self.eat(Tokens.Tokens.SUM) 
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.SUB:
                self.eat(Tokens.Tokens.SUB)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.MULT:
                self.eat(Tokens.Tokens.MULT)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.DIV:
                self.eat(Tokens.Tokens.DIV)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.POW:
                self.eat(Tokens.Tokens.POW)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.SQRT:
                self.eat(Tokens.Tokens.SQRT)
                result += " " + token.value + " " + self.atributionTypes()
        return result
        
    def VarAtrib(self):
        result = self.atributionTypes()
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.EQUAL, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                result += " " + token.value
            elif token.type == Tokens.Tokens.EQUAL:
                self.eat(Tokens.Tokens.EQUAL)
                result += " " + token.value + " " + self.atributionTypes()
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                result += " " + token.value
        return result

    def VarDecl(self):
        result = self.types()
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                result += " " + token.value
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                result += " " + token.value
            
        return result

    def types(self):
        result = ""
        while self.current_token.type in (Tokens.Tokens.STR, Tokens.Tokens.INT, Tokens.Tokens.FLT, Tokens.Tokens.BOOLEAN):
            token = self.current_token
            if token.type == Tokens.Tokens.STR:
                self.eat(Tokens.Tokens.STR)
                result = token.value
            elif token.type == Tokens.Tokens.INT:
                self.eat(Tokens.Tokens.INT)
                result = token.value
            elif token.type == Tokens.Tokens.FLT:
                self.eat(Tokens.Tokens.FLT)
                result = token.value
            elif token.type == Tokens.Tokens.BOOLEAN:
                self.eat(Tokens.Tokens.BOOLEAN)
                result = token.value
        return result

    def atributionTypes(self):
        result = ""
        while self.current_token.type in (Tokens.Tokens.STRING, Tokens.Tokens.INTEGER, Tokens.Tokens.FLOAT, Tokens.Tokens.BOOLEANTRUE, Tokens.Tokens.BOOLEANFALSE):
            token = self.current_token
            if token.type == Tokens.Tokens.STRING:
                self.eat(Tokens.Tokens.STRING)
                result = token.value
            elif token.type == Tokens.Tokens.INTEGER:
                self.eat(Tokens.Tokens.INTEGER)
                result = token.value
            elif token.type == Tokens.Tokens.FLOAT:
                self.eat(Tokens.Tokens.FLOAT)
                result = token.value
            elif token.type == Tokens.Tokens.BOOLEANTRUE:
                self.eat(Tokens.Tokens.BOOLEANTRUE)
                result = token.value
            elif token.type == Tokens.Tokens.BOOLEANFALSE:
                self.eat(Tokens.Tokens.BOOLEANFALSE)
                result = token.value
        return result

