# Generated from gr.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("w\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\5\2-\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\5\4\65\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6=\n\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tJ\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\rW\n\r")
        buf.write("\3\16\3\16\5\16[\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\5\21i\n\21\3\22\3\22\5\22")
        buf.write("m\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\2")
        buf.write("\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\3")
        buf.write("\4\2\3\f\17\21\2n\2,\3\2\2\2\4.\3\2\2\2\6\64\3\2\2\2\b")
        buf.write("\66\3\2\2\2\n<\3\2\2\2\f>\3\2\2\2\16A\3\2\2\2\20I\3\2")
        buf.write("\2\2\22K\3\2\2\2\24O\3\2\2\2\26Q\3\2\2\2\30V\3\2\2\2\32")
        buf.write("Z\3\2\2\2\34\\\3\2\2\2\36`\3\2\2\2 h\3\2\2\2\"l\3\2\2")
        buf.write("\2$n\3\2\2\2&r\3\2\2\2(t\3\2\2\2*-\5\4\3\2+-\5\6\4\2,")
        buf.write("*\3\2\2\2,+\3\2\2\2-\3\3\2\2\2./\5\6\4\2/\60\7\3\2\2\60")
        buf.write("\61\5\2\2\2\61\5\3\2\2\2\62\65\5\b\5\2\63\65\5\n\6\2\64")
        buf.write("\62\3\2\2\2\64\63\3\2\2\2\65\7\3\2\2\2\66\67\5\n\6\2\67")
        buf.write("8\5\6\4\28\t\3\2\2\29=\5\f\7\2:=\5\16\b\2;=\5\20\t\2<")
        buf.write("9\3\2\2\2<:\3\2\2\2<;\3\2\2\2=\13\3\2\2\2>?\5\20\t\2?")
        buf.write("@\7\4\2\2@\r\3\2\2\2AB\5\20\t\2BC\7\5\2\2C\17\3\2\2\2")
        buf.write("DJ\5\22\n\2EJ\5\24\13\2FJ\5\26\f\2GJ\5\30\r\2HJ\5\32\16")
        buf.write("\2ID\3\2\2\2IE\3\2\2\2IF\3\2\2\2IG\3\2\2\2IH\3\2\2\2J")
        buf.write("\21\3\2\2\2KL\7\6\2\2LM\5\2\2\2MN\7\7\2\2N\23\3\2\2\2")
        buf.write("OP\7\b\2\2P\25\3\2\2\2QR\7\t\2\2R\27\3\2\2\2SW\5(\25\2")
        buf.write("TU\7\n\2\2UW\5&\24\2VS\3\2\2\2VT\3\2\2\2W\31\3\2\2\2X")
        buf.write("[\5\34\17\2Y[\5\36\20\2ZX\3\2\2\2ZY\3\2\2\2[\33\3\2\2")
        buf.write("\2\\]\7\13\2\2]^\5 \21\2^_\7\f\2\2_\35\3\2\2\2`a\7\r\2")
        buf.write("\2ab\5 \21\2bc\7\f\2\2c\37\3\2\2\2di\5\"\22\2ef\5\"\22")
        buf.write("\2fg\5 \21\2gi\3\2\2\2hd\3\2\2\2he\3\2\2\2i!\3\2\2\2j")
        buf.write("m\5$\23\2km\5\30\r\2lj\3\2\2\2lk\3\2\2\2m#\3\2\2\2no\5")
        buf.write("\30\r\2op\7\16\2\2pq\5\30\r\2q%\3\2\2\2rs\t\2\2\2s\'\3")
        buf.write("\2\2\2tu\n\2\2\2u)\3\2\2\2\n,\64<IVZhl")
        return buf.getvalue()


class grParser ( Parser ):

    grammarFileName = "gr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'('", "')'", "'.'", 
                     "'$'", "'\\'", "'['", "']'", "'[^'", "'-'", "'^'", 
                     "'{'", "'}'" ]

    symbolicNames = [  ]

    RULE_re = 0
    RULE_union = 1
    RULE_simple_re = 2
    RULE_concat = 3
    RULE_basic_re = 4
    RULE_star = 5
    RULE_plus = 6
    RULE_elementary_re = 7
    RULE_group = 8
    RULE_any_ = 9
    RULE_eos = 10
    RULE_char = 11
    RULE_set_ = 12
    RULE_positive_set = 13
    RULE_negative_set = 14
    RULE_set_items = 15
    RULE_set_item = 16
    RULE_range_ = 17
    RULE_metachar = 18
    RULE_non_metachar = 19

    ruleNames =  [ "re", "union", "simple_re", "concat", "basic_re", "star", 
                   "plus", "elementary_re", "group", "any_", "eos", "char", 
                   "set_", "positive_set", "negative_set", "set_items", 
                   "set_item", "range_", "metachar", "non_metachar" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ReContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union(self):
            return self.getTypedRuleContext(grParser.UnionContext,0)


        def simple_re(self):
            return self.getTypedRuleContext(grParser.Simple_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_re

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRe" ):
                listener.enterRe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRe" ):
                listener.exitRe(self)




    def re(self):

        localctx = grParser.ReContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_re)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.union()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.simple_re()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_re(self):
            return self.getTypedRuleContext(grParser.Simple_reContext,0)


        def re(self):
            return self.getTypedRuleContext(grParser.ReContext,0)


        def getRuleIndex(self):
            return grParser.RULE_union

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)




    def union(self):

        localctx = grParser.UnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_union)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.simple_re()
            self.state = 45
            self.match(grParser.T__0)
            self.state = 46
            self.re()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_reContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat(self):
            return self.getTypedRuleContext(grParser.ConcatContext,0)


        def basic_re(self):
            return self.getTypedRuleContext(grParser.Basic_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_simple_re

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_re" ):
                listener.enterSimple_re(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_re" ):
                listener.exitSimple_re(self)




    def simple_re(self):

        localctx = grParser.Simple_reContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_re)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.concat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.basic_re()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_re(self):
            return self.getTypedRuleContext(grParser.Basic_reContext,0)


        def simple_re(self):
            return self.getTypedRuleContext(grParser.Simple_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)




    def concat(self):

        localctx = grParser.ConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.basic_re()
            self.state = 53
            self.simple_re()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_reContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star(self):
            return self.getTypedRuleContext(grParser.StarContext,0)


        def plus(self):
            return self.getTypedRuleContext(grParser.PlusContext,0)


        def elementary_re(self):
            return self.getTypedRuleContext(grParser.Elementary_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_basic_re

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_re" ):
                listener.enterBasic_re(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_re" ):
                listener.exitBasic_re(self)




    def basic_re(self):

        localctx = grParser.Basic_reContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_basic_re)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.plus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.elementary_re()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementary_re(self):
            return self.getTypedRuleContext(grParser.Elementary_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)




    def star(self):

        localctx = grParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_star)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.elementary_re()
            self.state = 61
            self.match(grParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementary_re(self):
            return self.getTypedRuleContext(grParser.Elementary_reContext,0)


        def getRuleIndex(self):
            return grParser.RULE_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)




    def plus(self):

        localctx = grParser.PlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_plus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.elementary_re()
            self.state = 64
            self.match(grParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elementary_reContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(grParser.GroupContext,0)


        def any_(self):
            return self.getTypedRuleContext(grParser.Any_Context,0)


        def eos(self):
            return self.getTypedRuleContext(grParser.EosContext,0)


        def char(self):
            return self.getTypedRuleContext(grParser.CharContext,0)


        def set_(self):
            return self.getTypedRuleContext(grParser.Set_Context,0)


        def getRuleIndex(self):
            return grParser.RULE_elementary_re

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementary_re" ):
                listener.enterElementary_re(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementary_re" ):
                listener.exitElementary_re(self)




    def elementary_re(self):

        localctx = grParser.Elementary_reContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elementary_re)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.any_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.eos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.char()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.set_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def re(self):
            return self.getTypedRuleContext(grParser.ReContext,0)


        def getRuleIndex(self):
            return grParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)




    def group(self):

        localctx = grParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(grParser.T__3)
            self.state = 74
            self.re()
            self.state = 75
            self.match(grParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grParser.RULE_any_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_" ):
                listener.enterAny_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_" ):
                listener.exitAny_(self)




    def any_(self):

        localctx = grParser.Any_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_any_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(grParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = grParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_eos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(grParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_metachar(self):
            return self.getTypedRuleContext(grParser.Non_metacharContext,0)


        def metachar(self):
            return self.getTypedRuleContext(grParser.MetacharContext,0)


        def getRuleIndex(self):
            return grParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = grParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_char)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grParser.T__10, grParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.non_metachar()
                pass
            elif token in [grParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(grParser.T__7)
                self.state = 83
                self.metachar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positive_set(self):
            return self.getTypedRuleContext(grParser.Positive_setContext,0)


        def negative_set(self):
            return self.getTypedRuleContext(grParser.Negative_setContext,0)


        def getRuleIndex(self):
            return grParser.RULE_set_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_" ):
                listener.enterSet_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_" ):
                listener.exitSet_(self)




    def set_(self):

        localctx = grParser.Set_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_set_)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.positive_set()
                pass
            elif token in [grParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.negative_set()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Positive_setContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_items(self):
            return self.getTypedRuleContext(grParser.Set_itemsContext,0)


        def getRuleIndex(self):
            return grParser.RULE_positive_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositive_set" ):
                listener.enterPositive_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositive_set" ):
                listener.exitPositive_set(self)




    def positive_set(self):

        localctx = grParser.Positive_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_positive_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(grParser.T__8)
            self.state = 91
            self.set_items()
            self.state = 92
            self.match(grParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Negative_setContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_items(self):
            return self.getTypedRuleContext(grParser.Set_itemsContext,0)


        def getRuleIndex(self):
            return grParser.RULE_negative_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative_set" ):
                listener.enterNegative_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative_set" ):
                listener.exitNegative_set(self)




    def negative_set(self):

        localctx = grParser.Negative_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_negative_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(grParser.T__10)
            self.state = 95
            self.set_items()
            self.state = 96
            self.match(grParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_item(self):
            return self.getTypedRuleContext(grParser.Set_itemContext,0)


        def set_items(self):
            return self.getTypedRuleContext(grParser.Set_itemsContext,0)


        def getRuleIndex(self):
            return grParser.RULE_set_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_items" ):
                listener.enterSet_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_items" ):
                listener.exitSet_items(self)




    def set_items(self):

        localctx = grParser.Set_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_set_items)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.set_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.set_item()
                self.state = 100
                self.set_items()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_(self):
            return self.getTypedRuleContext(grParser.Range_Context,0)


        def char(self):
            return self.getTypedRuleContext(grParser.CharContext,0)


        def getRuleIndex(self):
            return grParser.RULE_set_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_item" ):
                listener.enterSet_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_item" ):
                listener.exitSet_item(self)




    def set_item(self):

        localctx = grParser.Set_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_set_item)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.char()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grParser.CharContext)
            else:
                return self.getTypedRuleContext(grParser.CharContext,i)


        def getRuleIndex(self):
            return grParser.RULE_range_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_" ):
                listener.enterRange_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_" ):
                listener.exitRange_(self)




    def range_(self):

        localctx = grParser.Range_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_range_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.char()
            self.state = 109
            self.match(grParser.T__11)
            self.state = 110
            self.char()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetacharContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grParser.RULE_metachar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetachar" ):
                listener.enterMetachar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetachar" ):
                listener.exitMetachar(self)




    def metachar(self):

        localctx = grParser.MetacharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_metachar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grParser.T__0) | (1 << grParser.T__1) | (1 << grParser.T__2) | (1 << grParser.T__3) | (1 << grParser.T__4) | (1 << grParser.T__5) | (1 << grParser.T__6) | (1 << grParser.T__7) | (1 << grParser.T__8) | (1 << grParser.T__9) | (1 << grParser.T__12) | (1 << grParser.T__13) | (1 << grParser.T__14))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_metacharContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grParser.RULE_non_metachar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_metachar" ):
                listener.enterNon_metachar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_metachar" ):
                listener.exitNon_metachar(self)




    def non_metachar(self):

        localctx = grParser.Non_metacharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_non_metachar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grParser.T__0) | (1 << grParser.T__1) | (1 << grParser.T__2) | (1 << grParser.T__3) | (1 << grParser.T__4) | (1 << grParser.T__5) | (1 << grParser.T__6) | (1 << grParser.T__7) | (1 << grParser.T__8) | (1 << grParser.T__9) | (1 << grParser.T__12) | (1 << grParser.T__13) | (1 << grParser.T__14))) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





