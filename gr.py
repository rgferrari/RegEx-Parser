from antlr4 import *
from grLexer import grLexer
from grListener import grListener
from grParser import grParser
import sys

def main():
    lexer = grLexer(InputStream(input('Poe a ER caralho: ')))
    #lexer = grLexer(InputStream('a*b*'))
    stream = CommonTokenStream(lexer)
    parser = grParser(stream)
    tree = parser.re()
    printer = tree.toStringTree(recog=parser)
    print(printer)

if __name__ == '__main__':
    main()

