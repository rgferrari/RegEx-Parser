from antlr4 import *
from grLexer import grLexer
from grListener import grListener
from grParser import grParser
from grPostfix import regexToPostfix
from automata import toNFA, match
from antlr4.error.ErrorListener import ErrorListener
import sys


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print ("ER invalida!")
        sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print ("ER invalida!")
        sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print ("ER invalida!")
        sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print ("ER invalida!")
        sys.exit()

def main():
    regex = input('Insira a ER: ')
    #regex = 'a*(b|a)'
    lexer = grLexer(InputStream(regex))
    #lexer = grLexer(InputStream('a')
    stream = CommonTokenStream(lexer)
    parser = grParser(stream)
    parser._listeners = [MyErrorListener()]
    tree = parser.re()
    printer = tree.toStringTree(recog=parser)
    print('ER Válida!')
    print('Arvore de derivação: '+printer)

    postfix = regexToPostfix(regex)
    nfa = toNFA(postfix)
    try:
        while True:
            if match(nfa, input('Insira a palavra a ser testada: ')):
                print("A palavra está dentro da ER apresentada!")
            else:
                print('A palavra não está dentro da ER apresentada!')
    except KeyboardInterrupt:
        print('\nSaindo...')
        sys.exit()

if __name__ == '__main__':
    main()