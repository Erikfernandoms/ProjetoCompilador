from Interpreter.Interpreter import Interpreter
from AnSint.Parser import Parser
from AnSint.Lexer import Lexer


def open_arq(arq):
        file = open(arq)
        word = file.read()
        return word

def main():
    lexer = Lexer(open_arq("teste.txt"))
    parser = Parser(lexer)
    interpreter = Interpreter(parser).interpreter()
    result = interpreter
    print(result)
    
if __name__ == "__main__":
  main()