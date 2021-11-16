from Interpreter.NodeVisitor import NodeVisitor
import Tokens.Tokens
import math

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        
    def visit_BinOp(self, node):
        if node.op.type == Tokens.Tokens.SUM:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Tokens.Tokens.SUB:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Tokens.Tokens.MULT:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Tokens.Tokens.DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == Tokens.Tokens.POW:
            return self.visit(node.left) ** self.visit(node.right)
        elif node.op.type == Tokens.Tokens.SQRT:
            return math.sqrt(self.visit(node.left)**self.visit(node.right))
        
    def visit_RelOp(self, node):
        if node.op.type == Tokens.Tokens.ESQMAIOR:
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == Tokens.Tokens.DIRMAIOR:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == Tokens.Tokens.ESQME:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == Tokens.Tokens.DIRME:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == Tokens.Tokens.DIF:
            return self.visit(node.left) != self.visit(node.right)
        elif node.op.type == Tokens.Tokens.EQUAL:
            return self.visit(node.left) == self.visit(node.right)

    def visit_VarAtrib(self, node):
        return node.value
    
    def visit_VarDecl(self, node):
        return node.value
    
    def visit_Num(self, node):
        return node.value
    
    def visit_BoolOp(self, node):
        return node.value

    def visit_Conditionals(self, node):
        return node.conditional

    def visit_ConstantTypes(self, node):
        return node.value
    
    def visit_Identifier(self, node):
        return node.value
    
    def visit_Operators(self, node):
        return node.value
    
    def visit_Statement(self, node):
        node = node.VarDecl, node.VarAtrib, node.types, node.atribuitionTypes, node.RelOp, node.Op, node.Operators
        for i in node:
            if i != '':
                return i
    
    def visit_STR(self, node):
        return node.value
    
    def interpreter(self):
        tree = self.parser.parse()
        return self.visit(tree)
