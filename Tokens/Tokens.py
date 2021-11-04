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

