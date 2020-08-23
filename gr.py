from antlr4 import *
from grLexer import grLexer
from grListener import grListener
from grParser import grParser

def main():
    regex = input('Insira a ER: ')
    #regex = 'a*(b|a)'
    lexer = grLexer(InputStream(regex))
    #lexer = grLexer(InputStream('a')
    stream = CommonTokenStream(lexer)
    parser = grParser(stream)
    tree = parser.re()
    printer = tree.toStringTree(recog=parser)
    print(printer)

if __name__ == '__main__':
    main()

    #a(a+b)*b