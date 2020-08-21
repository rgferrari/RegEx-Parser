# Generated from gr.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\2\2")
        buf.write("\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21\3\2\2\2?\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2")
        buf.write("\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61")
        buf.write("\3\2\2\2\25\63\3\2\2\2\27\65\3\2\2\2\318\3\2\2\2\33:\3")
        buf.write("\2\2\2\35<\3\2\2\2\37>\3\2\2\2!\"\7~\2\2\"\4\3\2\2\2#")
        buf.write("$\7,\2\2$\6\3\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7*\2\2(\n\3")
        buf.write("\2\2\2)*\7+\2\2*\f\3\2\2\2+,\7\60\2\2,\16\3\2\2\2-.\7")
        buf.write("&\2\2.\20\3\2\2\2/\60\7^\2\2\60\22\3\2\2\2\61\62\7]\2")
        buf.write("\2\62\24\3\2\2\2\63\64\7_\2\2\64\26\3\2\2\2\65\66\7]\2")
        buf.write("\2\66\67\7`\2\2\67\30\3\2\2\289\7/\2\29\32\3\2\2\2:;\7")
        buf.write("`\2\2;\34\3\2\2\2<=\7}\2\2=\36\3\2\2\2>?\7\177\2\2? \3")
        buf.write("\2\2\2\3\2\2")
        return buf.getvalue()


class grLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'*'", "'+'", "'('", "')'", "'.'", "'$'", "'\\'", "'['", 
            "']'", "'[^'", "'-'", "'^'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14" ]

    grammarFileName = "gr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


