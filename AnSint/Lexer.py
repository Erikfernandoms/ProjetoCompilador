import Tokens.Tokens, re

STR,INT,FLT,BOOLEAN,BOOLEANTRUE,BOOLEANFALSE,SUM,SUB,DIV,POW,MULT,EQUAL,SQRT,IF,ELSE,ELIF,WHILE,FOR,BREAK,FUNCTION,CLASS,COMMENT,IDENTIFIER,INTEGER,FLOAT,STRING,DIRPARENT,ESQPARENT,TWOPOINTS,ENDEXPRESSION,ESQMAIOR,DIRMAIOR,ESQME,DIRME,DIF,ESQKEY,DIRKEY,EQUALCOMP,AND,OR,NOT,EOF = ('string','int','float','boolean','true','false','+','-','/','^','*','=','|','if','else','elif','while','for','brk','func','class',"^'[A-Za-z0-9 ,.&]+'",'[A-Za-z]+$','^-?\d*?\d+$','(?:\.|,|[0-9])*','^"[A-Za-z0-9 ,._]+"','(',')',':',';','<','>','<=','>=','!=','{','}','==','and','or','not','EOF')#IDENTIFIER,INTEGER,FLOAT, REGEX

class Lexer(object):

    def __init__(self, elements):
        self.pos = 0
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
                return(Tokens.Tokens.Token(STR, "string"))
            elif caracters[self.pos] == "int":
                self.advance()
                return(Tokens.Tokens.Token(INT, "int"))
            elif caracters[self.pos] == "float":
                self.advance()
                return(Tokens.Tokens.Token(FLT, "float"))
            elif caracters[self.pos] == "True":
                self.advance()
                return(Tokens.Tokens.Token(BOOLEANTRUE, "true"))
            elif caracters[self.pos] == "boolean":
                self.advance()
                return(Tokens.Tokens.Token(BOOLEAN, "boolean"))
            elif caracters[self.pos] == "False":
                self.advance()
                return(Tokens.Tokens.Token(BOOLEANFALSE, "false"))
            elif caracters[self.pos] == "+":
                self.advance()
                return(Tokens.Tokens.Token(SUM, "+"))
            elif caracters[self.pos] == ":":
                self.advance()
                return(Tokens.Tokens.Token(TWOPOINTS, ":"))
            elif caracters[self.pos] == "-": 
                self.advance()
                return(Tokens.Tokens.Token(SUB, "-"))
            elif caracters[self.pos] == "/":   
                self.advance()
                return(Tokens.Tokens.Token(DIV, "/"))
            elif caracters[self.pos] == ";":  
                self.advance()
                return(Tokens.Tokens.Token(ENDEXPRESSION, "endexpression"))
            elif caracters[self.pos] == "^":  
                self.advance()
                return(Tokens.Tokens.Token(POW, "^"))
            elif caracters[self.pos] == "*":    
                self.advance()
                return(Tokens.Tokens.Token(MULT, "*"))
            elif caracters[self.pos] == "=":
                self.advance()
                return(Tokens.Tokens.Token(EQUAL, "="))
            elif caracters[self.pos] == "<":                
                self.advance()
                return(Tokens.Tokens.Token(ESQMAIOR, "<"))
            elif caracters[self.pos] == ">":               
                self.advance()
                return(Tokens.Tokens.Token(DIRMAIOR, ">"))
            elif caracters[self.pos] == "=>":               
                self.advance()
                return(Tokens.Tokens.Token(DIRME, "=>"))
            elif caracters[self.pos] == "<=":                
                self.advance()
                return(Tokens.Tokens.Token(ESQME, "<="))
            elif caracters[self.pos] == "!=":                
                self.advance()
                return(Tokens.Tokens.Token(DIF, "!="))
            elif caracters[self.pos] == "(":               
                self.advance()
                return(Tokens.Tokens.Token(ESQPARENT, "("))
            elif caracters[self.pos] == ")":                
                self.advance()
                return(Tokens.Tokens.Token(DIRPARENT, ")"))
            elif caracters[self.pos] == "{":               
                self.advance()
                return(Tokens.Tokens.Token(ESQKEY, "{"))
            elif caracters[self.pos] == "}":               
                self.advance()
                return(Tokens.Tokens.Token(DIRKEY, "}"))
            elif caracters[self.pos] == "|":                
                self.advance()
                return(Tokens.Tokens.Token(SQRT, "sqrt"))
            elif caracters[self.pos] == "if":              
                self.advance()
                return(Tokens.Tokens.Token(IF, "if"))
            elif caracters[self.pos] == "else":              
                self.advance()
                return(Tokens.Tokens.Token(ELSE, "else"))
            elif caracters[self.pos] == "elif":               
                self.advance()
                return(Tokens.Tokens.Token(ELIF, "elif"))
            elif caracters[self.pos] == "while":              
                self.advance()
                return(Tokens.Tokens.Token(WHILE, "while"))
            elif caracters[self.pos] == "for":             
                self.advance()
                return(Tokens.Tokens.Token(FOR, "for"))
            elif caracters[self.pos] == "brk":             
                self.advance()
                return(Tokens.Tokens.Token(BREAK, "break"))
            elif caracters[self.pos] == "func":            
                self.advance()
                return(Tokens.Tokens.Token(FUNCTION, "function"))
            elif caracters[self.pos] == "==":            
                self.advance()
                return(Tokens.Tokens.Token(EQUALCOMP, "=="))
            elif caracters[self.pos] == "and":            
                self.advance()
                return(Tokens.Tokens.Token(AND, "and"))
            elif caracters[self.pos] == "or":            
                self.advance()
                return(Tokens.Tokens.Token(OR, "or"))
            elif caracters[self.pos] == "not":            
                self.advance()
                return(Tokens.Tokens.Token(NOT, "not"))
            elif caracters[self.pos] == "class":            
                self.advance()
                return(Tokens.Tokens.Token(CLASS, "class"))
            elif re.match(r"^'[A-Za-z0-9 ,.&]+'", caracters[self.pos]):           
                self.advance()
                return(Tokens.Tokens.Token(COMMENT, "comment"))
            elif caracters[self.pos] == '':  
                self.advance()
            elif re.match(r'[A-Za-z]+$', caracters[self.pos]):     
                self.advance()
                return(Tokens.Tokens.Token(IDENTIFIER, "identifier"))
            elif re.match(r'^"[A-Za-z0-9 ,._]+"', caracters[self.pos]):               
                self.advance()
                return(Tokens.Tokens.Token(STRING, "string"))
            elif re.match(r'^-?\d*?\d+$', caracters[self.pos]):     
                self.advance()
                return(Tokens.Tokens.Token(INTEGER, "integer"))
            elif re.match(r'^\d+(\,\d{1,10})?$', caracters[self.pos]):  
                self.advance()
                return(Tokens.Tokens.Token(FLOAT, "float"))
            else:
                self.error()        
        return Tokens.Tokens.Token(EOF, None)

    def error(self):
        raise Exception("Invalid character!")