from antlr4 import *
from grLexer import grLexer
from grListener import grListener
from grParser import grParser
import sys

class GrPrintListener(grListener):
    def enterRegEx(self, ctx):
        print("RegEx: %s" % ctx.re())

def main():
    lexer = grLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = grParser(stream)
    tree = parser.re()
    printer = GrPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()

