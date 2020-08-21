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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\5\4)\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t=\n\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\rJ\n\r\3\16\3\16\3")
        buf.write("\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\2\4\3\2\3\17\3\2\20)\2I\2 \3\2\2\2\4\"\3\2\2\2\6(")
        buf.write("\3\2\2\2\b*\3\2\2\2\n\60\3\2\2\2\f\62\3\2\2\2\16\65\3")
        buf.write("\2\2\2\20<\3\2\2\2\22>\3\2\2\2\24B\3\2\2\2\26D\3\2\2\2")
        buf.write("\30I\3\2\2\2\32K\3\2\2\2\34M\3\2\2\2\36!\5\4\3\2\37!\5")
        buf.write("\6\4\2 \36\3\2\2\2 \37\3\2\2\2!\3\3\2\2\2\"#\5\6\4\2#")
        buf.write("$\7\3\2\2$%\5\2\2\2%\5\3\2\2\2&)\5\b\5\2\')\5\n\6\2(&")
        buf.write("\3\2\2\2(\'\3\2\2\2)\7\3\2\2\2*+\5\n\6\2+,\5\6\4\2,\t")
        buf.write("\3\2\2\2-\61\5\f\7\2.\61\5\16\b\2/\61\5\20\t\2\60-\3\2")
        buf.write("\2\2\60.\3\2\2\2\60/\3\2\2\2\61\13\3\2\2\2\62\63\5\20")
        buf.write("\t\2\63\64\7\4\2\2\64\r\3\2\2\2\65\66\5\20\t\2\66\67\7")
        buf.write("\5\2\2\67\17\3\2\2\28=\5\22\n\29=\5\24\13\2:=\5\26\f\2")
        buf.write(";=\5\30\r\2<8\3\2\2\2<9\3\2\2\2<:\3\2\2\2<;\3\2\2\2=\21")
        buf.write("\3\2\2\2>?\7\6\2\2?@\5\2\2\2@A\7\7\2\2A\23\3\2\2\2BC\7")
        buf.write("\b\2\2C\25\3\2\2\2DE\7\t\2\2E\27\3\2\2\2FJ\5\34\17\2G")
        buf.write("H\7\n\2\2HJ\5\32\16\2IF\3\2\2\2IG\3\2\2\2J\31\3\2\2\2")
        buf.write("KL\t\2\2\2L\33\3\2\2\2MN\t\3\2\2N\35\3\2\2\2\7 (\60<I")
        return buf.getvalue()


class grParser ( Parser ):

    grammarFileName = "gr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'('", "')'", "'.'", 
                     "'$'", "'\\'", "'['", "']'", "'^'", "'{'", "'}'", "'a'", 
                     "'b'", "'c'", "'d'", "'e'", "'f'", "'g'", "'h'", "'i'", 
                     "'j'", "'k'", "'l'", "'m'", "'n'", "'o'", "'p'", "'q'", 
                     "'r'", "'s'", "'t'", "'u'", "'v'", "'w'", "'x'", "'y'", 
                     "'z'" ]

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
    RULE_char_ = 11
    RULE_metachar = 12
    RULE_non_metachar = 13

    ruleNames =  [ "re", "union", "simple_re", "concat", "basic_re", "star", 
                   "plus", "elementary_re", "group", "any_", "eos", "char_", 
                   "metachar", "non_metachar" ]

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
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39

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
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.union()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
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
            self.state = 32
            self.simple_re()
            self.state = 33
            self.match(grParser.T__0)
            self.state = 34
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.concat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
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
            self.state = 40
            self.basic_re()
            self.state = 41
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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.plus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
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
            self.state = 48
            self.elementary_re()
            self.state = 49
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
            self.state = 51
            self.elementary_re()
            self.state = 52
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


        def char_(self):
            return self.getTypedRuleContext(grParser.Char_Context,0)


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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.group()
                pass
            elif token in [grParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.any_()
                pass
            elif token in [grParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.eos()
                pass
            elif token in [grParser.T__7, grParser.T__13, grParser.T__14, grParser.T__15, grParser.T__16, grParser.T__17, grParser.T__18, grParser.T__19, grParser.T__20, grParser.T__21, grParser.T__22, grParser.T__23, grParser.T__24, grParser.T__25, grParser.T__26, grParser.T__27, grParser.T__28, grParser.T__29, grParser.T__30, grParser.T__31, grParser.T__32, grParser.T__33, grParser.T__34, grParser.T__35, grParser.T__36, grParser.T__37, grParser.T__38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.char_()
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
            self.state = 60
            self.match(grParser.T__3)
            self.state = 61
            self.re()
            self.state = 62
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
            self.state = 64
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
            self.state = 66
            self.match(grParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Char_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_metachar(self):
            return self.getTypedRuleContext(grParser.Non_metacharContext,0)


        def metachar(self):
            return self.getTypedRuleContext(grParser.MetacharContext,0)


        def getRuleIndex(self):
            return grParser.RULE_char_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_" ):
                listener.enterChar_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_" ):
                listener.exitChar_(self)




    def char_(self):

        localctx = grParser.Char_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_char_)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grParser.T__13, grParser.T__14, grParser.T__15, grParser.T__16, grParser.T__17, grParser.T__18, grParser.T__19, grParser.T__20, grParser.T__21, grParser.T__22, grParser.T__23, grParser.T__24, grParser.T__25, grParser.T__26, grParser.T__27, grParser.T__28, grParser.T__29, grParser.T__30, grParser.T__31, grParser.T__32, grParser.T__33, grParser.T__34, grParser.T__35, grParser.T__36, grParser.T__37, grParser.T__38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.non_metachar()
                pass
            elif token in [grParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(grParser.T__7)
                self.state = 70
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
        self.enterRule(localctx, 24, self.RULE_metachar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grParser.T__0) | (1 << grParser.T__1) | (1 << grParser.T__2) | (1 << grParser.T__3) | (1 << grParser.T__4) | (1 << grParser.T__5) | (1 << grParser.T__6) | (1 << grParser.T__7) | (1 << grParser.T__8) | (1 << grParser.T__9) | (1 << grParser.T__10) | (1 << grParser.T__11) | (1 << grParser.T__12))) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_non_metachar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grParser.T__13) | (1 << grParser.T__14) | (1 << grParser.T__15) | (1 << grParser.T__16) | (1 << grParser.T__17) | (1 << grParser.T__18) | (1 << grParser.T__19) | (1 << grParser.T__20) | (1 << grParser.T__21) | (1 << grParser.T__22) | (1 << grParser.T__23) | (1 << grParser.T__24) | (1 << grParser.T__25) | (1 << grParser.T__26) | (1 << grParser.T__27) | (1 << grParser.T__28) | (1 << grParser.T__29) | (1 << grParser.T__30) | (1 << grParser.T__31) | (1 << grParser.T__32) | (1 << grParser.T__33) | (1 << grParser.T__34) | (1 << grParser.T__35) | (1 << grParser.T__36) | (1 << grParser.T__37) | (1 << grParser.T__38))) != 0)):
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





