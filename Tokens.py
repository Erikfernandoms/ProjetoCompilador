########################################################
##  Nome: Erik Fernando Mendes Silva RA: 22.119.074-7 ##
##  Nome: Lucas Medeiros RA: 22.119.057-2  ##
##  Nome: Vanessa Gomes RA: 22.119.009-3 ##
##  Nome: Bruno Jovenasso RA: 22.119.020-0 ##
########################################################

#       TOKENS      #     LEXEMAS     #
#######################################
#   
#       INT         #       INT
#       FLOAT       #       FLOAT
#       DOUBLE      #       DOUBLE
#       STR         #       s
#       INT         #       int
#       FLOAT       #       float
#       STRING      #       ^"[A-Za-z0-9 ,._]+"
#       INTEGER     #       ^-?\d*?\d+$
#       FLOAT       #       (?:\.|,|[0-9])*
#       BOOLEANTRUE #       TRUE
#       BOOLEANFALSE#       FALSE
#       SUM         #       +
#       SUB         #       -
#       DIV         #       /
#       POW         #       ^
#       MULT        #       * 
#       SQRT        #       |
#       IF          #       if
#       ELSE        #       else
#       ELIF        #       elif
#       WHILE       #       while
#       FOR         #       for
#       BREAK       #       brk
#       FUNCTION    #       func
#       CLASS       #       class       
#       COMMENT     #        ^'[A-Za-z0-9 ,.&]+'
#       DIRPARENT   #        (
#       ESQPARENT   #         )
#
#######################################

#EXPLICAÇÃO DOS TOKENS
######################
#   STRING -> Tipo para texto ou cadeias de caracteres.
#   BOOLEAN -> Tipo para booleanos.
#   SUM -> Tipo Operação de soma.
#   SUB -> Tipo Operação de subtração.
#   DIV -> Tipo Operação de divisão.
#   POW -> Tipo Operação de potência.
#   MULT -> Tipo Operação de multiplicação.
#   SQRT -> Tipo Operação de racionalização.
#   MODULE -> Tipo Operação de modularização.
#   IF -> Tipo condicional.
#   ELSE -> Tipo de condicional.
#   ELIF -> Tipo de condicional.
#   WHILE -> Tipo de repetição.
#   FOR -> Tipo Laço de repetição.
#   BREAK -> Tipo de quebra dos laços de repetição.
#   FUNCTION -> Tipo de uma função.
#   CLASS -> Tipo de uma classe.
#   COMMENT -> Tipo comentário.
#   IDENTIFIER -> Tipo identificador.
#   STR -> Tipo String.
#   INT -> Tipo inteiros.
#   FLOAT -> Tipo flutuantes.
#   INTEGER -> Qualquer numero real.
#   FLOAT -> Qualquer numero flutuante (separado com ponto).
#
######################

#           VARIAVEIS
######################
#
#   Definição de variáveis
#
#
#   LEXEMA -> REGEX [A-Za-z]+$ -> Reconhece qualquer letra de A-Z ou a-z e qualquer numero de 0-9, não reconhecendo carcteres especiais.
#   TOKEN -> IDENTIFIER
#
#####################

STR,INT,FLT,BOOLEAN,BOOLEANTRUE,BOOLEANFALSE,SUM,SUB,DIV,POW,MULT,EQUAL,SQRT,IF,ELSE,ELIF,WHILE,FOR,BREAK,FUNCTION,CLASS,COMMENT,IDENTIFIER,INTEGER,FLOAT,STRING,DIRPARENT,ESQPARENT,TWOPOINTS,ENDEXPRESSION,ESQMAIOR,DIRMAIOR,ESQME,DIRME,DIF,ESQKEY,DIRKEY,EQUALCOMP,AND,OR,NOT,EOF = ('string','int','float','boolean','true','false','+','-','/','^','*','=','|','if','else','elif','while','for','brk','func','class',"^'[A-Za-z0-9 ,.&]+'",'[A-Za-z]+$','^-?\d*?\d+$','(?:\.|,|[0-9])*','^"[A-Za-z0-9 ,._]+"','(',')',':',';','<','>','<=','>=','!=','{','}','==','and','or','not','EOF')#IDENTIFIER,INTEGER,FLOAT, REGEX
import re

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value
  
    def __str__(self):
        return "Token: ({type},{value})".format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return self.__str__()

    def getType(self):
        return self.type


class Lexer:

    def __init__(self, elements):
        self.pos = 0
        self.tokens = []
        self.elements = elements

    def advance(self):
        self.pos += 1
        if self.pos > len(self.elements) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.elements[self.pos]

    def getToken(self):
        caracters = re.split(' |\n', self.elements)
        while self.pos < len(caracters):
            if caracters[self.pos] == "string":
                self.advance()
                return(Token(STR, "string"))
            elif caracters[self.pos] == "int":
                self.advance()
                return(Token(INT, "int"))
            elif caracters[self.pos] == "float":
                self.advance()
                return(Token(FLT, "float"))
            elif caracters[self.pos] == "True":
                self.advance()
                return(Token(BOOLEANTRUE, "true"))
            elif caracters[self.pos] == "boolean":
                self.advance()
                return(Token(BOOLEAN, "boolean"))
            elif caracters[self.pos] == "False":
                self.advance()
                return(Token(BOOLEANFALSE, "false"))
            elif caracters[self.pos] == "+":
                self.advance()
                return(Token(SUM, "+"))
            elif caracters[self.pos] == ":":
                self.advance()
                return(Token(TWOPOINTS, ":"))
            elif caracters[self.pos] == "-": 
                self.advance()
                return(Token(SUB, "-"))
            elif caracters[self.pos] == "/":   
                self.advance()
                return(Token(DIV, "/"))
            elif caracters[self.pos] == ";":  
                self.advance()
                return(Token(ENDEXPRESSION, "endexpression"))
            elif caracters[self.pos] == "^":  
                self.advance()
                return(Token(POW, "^"))
            elif caracters[self.pos] == "*":    
                self.advance()
                return(Token(MULT, "*"))
            elif caracters[self.pos] == "=":
                self.advance()
                return(Token(EQUAL, "="))
            elif caracters[self.pos] == "<":                
                self.advance()
                return(Token(ESQMAIOR, "<"))
            elif caracters[self.pos] == ">":               
                self.advance()
                return(Token(DIRMAIOR, ">"))
            elif caracters[self.pos] == "=>":               
                self.advance()
                return(Token(DIRME, "=>"))
            elif caracters[self.pos] == "<=":                
                self.advance()
                return(Token(ESQME, "<="))
            elif caracters[self.pos] == "!=":                
                self.advance()
                return(Token(DIF, "!="))
            elif caracters[self.pos] == "(":               
                self.advance()
                return(Token(ESQPARENT, "("))
            elif caracters[self.pos] == ")":                
                self.advance()
                return(Token(DIRPARENT, ")"))
            elif caracters[self.pos] == "{":               
                self.advance()
                return(Token(ESQKEY, "{"))
            elif caracters[self.pos] == "}":               
                self.advance()
                return(Token(DIRKEY, "}"))
            elif caracters[self.pos] == "|":                
                self.advance()
                return(Token(SQRT, "sqrt"))
            elif caracters[self.pos] == "if":              
                self.advance()
                return(Token(IF, "if"))
            elif caracters[self.pos] == "else":              
                self.advance()
                return(Token(ELSE, "else"))
            elif caracters[self.pos] == "elif":               
                self.advance()
                return(Token(ELIF, "elif"))
            elif caracters[self.pos] == "while":              
                self.advance()
                return(Token(WHILE, "while"))
            elif caracters[self.pos] == "for":             
                self.advance()
                return(Token(FOR, "for"))
            elif caracters[self.pos] == "brk":             
                self.advance()
                return(Token(BREAK, "break"))
            elif caracters[self.pos] == "func":            
                self.advance()
                return(Token(FUNCTION, "function"))
            elif caracters[self.pos] == "==":            
                self.advance()
                return(Token(EQUALCOMP, "=="))
            elif caracters[self.pos] == "and":            
                self.advance()
                return(Token(AND, "and"))
            elif caracters[self.pos] == "or":            
                self.advance()
                return(Token(OR, "or"))
            elif caracters[self.pos] == "not":            
                self.advance()
                return(Token(NOT, "not"))
            elif caracters[self.pos] == "class":            
                self.advance()
                return(Token(CLASS, "class"))
            elif re.match(r"^'[A-Za-z0-9 ,.&]+'", caracters[self.pos]):           
                self.advance()
                return(Token(COMMENT, "comment"))
            elif caracters[self.pos] == '':  
                if self.pos > len(caracters) - 1:
                    self.current_char = None
                else:
                    self.current_char = caracters[self.pos]
                continue
            elif re.match(r'[A-Za-z]+$', caracters[self.pos]):     
                self.advance()
                return(Token(IDENTIFIER, "identifier"))
            elif re.match(r'^"[A-Za-z0-9 ,._]+"', caracters[self.pos]):               
                self.advance()
                return(Token(STRING, "string"))
            elif re.match(r'^-?\d*?\d+$', caracters[self.pos]):     
                self.advance()
                return(Token(INTEGER, "integer"))
            elif re.match(r'^\d+(\,\d{1,10})?$', caracters[self.pos]):  
                self.advance()
                return(Token(FLOAT, "float"))
            else:
                self.error()        
        return Token(EOF, None)

    def error(self):
        raise Exception("Invalid character!")



            



