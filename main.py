import Interpreter.Interpreter, AnSint.Parser, AnSint.Lexer

def open_arq(arq):
        file = open(arq)
        word = file.read()
        return word

def main():
    lexer = AnSint.Lexer.Lexer(open_arq("teste.txt"))
    interpreter = AnSint.Parser.Parser(lexer)
    result = interpreter.Conditional()
    print(result)
    
if __name__ == "__main__":
  main()