import Interpreter.Interpreter, AnSint.Parser, AnSint.Lexer

def open_arq(arq):
        file = open(arq)
        word = file.read()
        return word

def main():
    lexer = AnSint.Lexer.Lexer(open_arq("teste.txt"))
    parser = AnSint.Parser.Parser(lexer)
    interpreter = Interpreter.Interpreter.Interpreter(parser).interpreter()
    result = interpreter
    print(result)
    
if __name__ == "__main__":
  main()