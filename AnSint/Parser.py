import re
from typing import List
import Tokens.Tokens
from Tree.Conditionals import Conditionals
from Tree.Num import Num
from Tree.BinOp import BinOp
from Tree.BoolOp import BoolOp
from Tree.Operators import Operators
from Tree.RelOp import RelOp
from Tree.Statement import Statement
from Tree.Str import Str
from Tree.ConstantTypes import ConstantTypes
from Tree.VarAtrib import VarAtrib
from Tree.VarDecl import VarDecl


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

    def parse(self):
        return self.Conditional()

    def Conditional(self):
        node = self.Statement()
        while self.current_token.type in (Tokens.Tokens.IF, Tokens.Tokens.ESQPARENT, Tokens.Tokens.DIRPARENT, Tokens.Tokens.TWOPOINTS,Tokens.Tokens.ELIF, Tokens.Tokens.ELSE, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IF:
                self.eat(Tokens.Tokens.IF)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.ESQPARENT:
                self.eat(Tokens.Tokens.ESQPARENT)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.DIRPARENT:
                self.eat(Tokens.Tokens.DIRPARENT)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.TWOPOINTS:
                self.eat(Tokens.Tokens.TWOPOINTS)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.ELIF:
                self.eat(Tokens.Tokens.ELIF)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.ELSE:
                self.eat(Tokens.Tokens.ELSE)
                node = Conditionals(token, self.Statement())
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                node = Conditionals(token, self.Statement())
        return node
    
    def Statement(self) -> list:
        node = Statement(self.VarDecl(), self.VarAtrib(), self.atributionTypes(), self.types(), self.RelOp(), self.Op(), self.Operators())
        return node
      
    def Operators(self):
        node = ""
        while self.current_token.type in (Tokens.Tokens.NOT, Tokens.Tokens.AND, Tokens.Tokens.OR):
            token = self.current_token
            if token.type == Tokens.Tokens.NOT:
                self.eat(Tokens.Tokens.NOT)
                node = Operators(token)
            elif token.type == Tokens.Tokens.AND:
                self.eat(Tokens.Tokens.AND)
                node = Operators(token)
            elif token.type == Tokens.Tokens.OR:
                self.eat(Tokens.Tokens.OR) 
                node = Operators(token)
        return node

    def RelOp(self):
        node = self.atributionTypes() 
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION,Tokens.Tokens.ESQMAIOR, Tokens.Tokens.DIRMAIOR, Tokens.Tokens.ESQME, Tokens.Tokens.DIRME, Tokens.Tokens.DIF, Tokens.Tokens.EQUALCOMP):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.ESQMAIOR:
                self.eat(Tokens.Tokens.ESQMAIOR) 
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.DIRMAIOR:
                self.eat(Tokens.Tokens.DIRMAIOR)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.ESQME:
                self.eat(Tokens.Tokens.ESQME)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.DIRME:
                self.eat(Tokens.Tokens.DIRME)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.DIF:
                self.eat(Tokens.Tokens.DIF)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.EQUAL:
                self.eat(Tokens.Tokens.EQUALCOMP)
                node = RelOp(left=node, op=token, right=self.atributionTypes())
        return node

    def Op(self):
        node = self.atributionTypes() 
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION,Tokens.Tokens.SUM, Tokens.Tokens.SUB, Tokens.Tokens.MULT, Tokens.Tokens.DIV, Tokens.Tokens.POW, Tokens.Tokens.SQRT):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.SUM:
                self.eat(Tokens.Tokens.SUM) 
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.SUB:
                self.eat(Tokens.Tokens.SUB)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.MULT:
                self.eat(Tokens.Tokens.MULT)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.DIV:
                self.eat(Tokens.Tokens.DIV)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.POW:
                self.eat(Tokens.Tokens.POW)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.SQRT:
                self.eat(Tokens.Tokens.SQRT)
                node = BinOp(left=node, op=token, right=self.atributionTypes())
        return node
        
    def VarAtrib(self):
        node = self.atributionTypes()
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.EQUAL, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                node = VarAtrib(left=node, atribuition=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.EQUAL:
                self.eat(Tokens.Tokens.EQUAL)
                node = VarAtrib(left=node, atribuition=token, right=self.atributionTypes())
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                node = VarAtrib(left=node, atribuition=token, right=self.atributionTypes())
        return node

    def VarDecl(self):
        node = self.types()
        while self.current_token.type in (Tokens.Tokens.IDENTIFIER, Tokens.Tokens.ENDEXPRESSION):
            token = self.current_token
            if token.type == Tokens.Tokens.IDENTIFIER:
                self.eat(Tokens.Tokens.IDENTIFIER)
                node = VarDecl(self.types(),token)
            elif token.type == Tokens.Tokens.ENDEXPRESSION:
                self.eat(Tokens.Tokens.ENDEXPRESSION)
                node = VarDecl(self.types(),token)
            
        return node

    def types(self):
        node = ""
        while self.current_token.type in (Tokens.Tokens.STR, Tokens.Tokens.INT, Tokens.Tokens.FLT, Tokens.Tokens.BOOLEAN):
            token = self.current_token
            if token.type == Tokens.Tokens.STR:
                self.eat(Tokens.Tokens.STR)
                node = ConstantTypes(token)
            elif token.type == Tokens.Tokens.INT:
                self.eat(Tokens.Tokens.INT)
                node = ConstantTypes(token)
            elif token.type == Tokens.Tokens.FLT:
                self.eat(Tokens.Tokens.FLT)
                node = ConstantTypes(token)
            elif token.type == Tokens.Tokens.BOOLEAN:
                self.eat(Tokens.Tokens.BOOLEAN)
                node = ConstantTypes(token)
        return node

    def atributionTypes(self):
        node = ""
        while self.current_token.type in (Tokens.Tokens.STRING, Tokens.Tokens.INTEGER, Tokens.Tokens.FLOAT, Tokens.Tokens.BOOLEANTRUE, Tokens.Tokens.BOOLEANFALSE):
            token = self.current_token
            if token.type == Tokens.Tokens.STRING:
                self.eat(Tokens.Tokens.STRING)
                node = Str(node)
            elif token.type == Tokens.Tokens.INTEGER:
                self.eat(Tokens.Tokens.INTEGER)
                node = Num(token)
            elif token.type == Tokens.Tokens.FLOAT:
                self.eat(Tokens.Tokens.FLOAT)
                node = Num(token)
            elif token.type == Tokens.Tokens.BOOLEANTRUE:
                self.eat(Tokens.Tokens.BOOLEANTRUE)
                node = BoolOp(token)
            elif token.type == Tokens.Tokens.BOOLEANFALSE:
                self.eat(Tokens.Tokens.BOOLEANFALSE)
                node = BoolOp(token)
        return node

