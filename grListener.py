# Generated from gr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grParser import grParser
else:
    from grParser import grParser

# This class defines a complete listener for a parse tree produced by grParser.
class grListener(ParseTreeListener):

    # Enter a parse tree produced by grParser#re.
    def enterRe(self, ctx:grParser.ReContext):
        pass

    # Exit a parse tree produced by grParser#re.
    def exitRe(self, ctx:grParser.ReContext):
        pass


    # Enter a parse tree produced by grParser#union.
    def enterUnion(self, ctx:grParser.UnionContext):
        pass

    # Exit a parse tree produced by grParser#union.
    def exitUnion(self, ctx:grParser.UnionContext):
        pass


    # Enter a parse tree produced by grParser#simple_re.
    def enterSimple_re(self, ctx:grParser.Simple_reContext):
        pass

    # Exit a parse tree produced by grParser#simple_re.
    def exitSimple_re(self, ctx:grParser.Simple_reContext):
        pass


    # Enter a parse tree produced by grParser#concat.
    def enterConcat(self, ctx:grParser.ConcatContext):
        pass

    # Exit a parse tree produced by grParser#concat.
    def exitConcat(self, ctx:grParser.ConcatContext):
        pass


    # Enter a parse tree produced by grParser#basic_re.
    def enterBasic_re(self, ctx:grParser.Basic_reContext):
        pass

    # Exit a parse tree produced by grParser#basic_re.
    def exitBasic_re(self, ctx:grParser.Basic_reContext):
        pass


    # Enter a parse tree produced by grParser#star.
    def enterStar(self, ctx:grParser.StarContext):
        pass

    # Exit a parse tree produced by grParser#star.
    def exitStar(self, ctx:grParser.StarContext):
        pass


    # Enter a parse tree produced by grParser#plus.
    def enterPlus(self, ctx:grParser.PlusContext):
        pass

    # Exit a parse tree produced by grParser#plus.
    def exitPlus(self, ctx:grParser.PlusContext):
        pass


    # Enter a parse tree produced by grParser#elementary_re.
    def enterElementary_re(self, ctx:grParser.Elementary_reContext):
        pass

    # Exit a parse tree produced by grParser#elementary_re.
    def exitElementary_re(self, ctx:grParser.Elementary_reContext):
        pass


    # Enter a parse tree produced by grParser#group.
    def enterGroup(self, ctx:grParser.GroupContext):
        pass

    # Exit a parse tree produced by grParser#group.
    def exitGroup(self, ctx:grParser.GroupContext):
        pass


    # Enter a parse tree produced by grParser#any_.
    def enterAny_(self, ctx:grParser.Any_Context):
        pass

    # Exit a parse tree produced by grParser#any_.
    def exitAny_(self, ctx:grParser.Any_Context):
        pass


    # Enter a parse tree produced by grParser#eos.
    def enterEos(self, ctx:grParser.EosContext):
        pass

    # Exit a parse tree produced by grParser#eos.
    def exitEos(self, ctx:grParser.EosContext):
        pass


    # Enter a parse tree produced by grParser#char.
    def enterChar(self, ctx:grParser.CharContext):
        pass

    # Exit a parse tree produced by grParser#char.
    def exitChar(self, ctx:grParser.CharContext):
        pass


    # Enter a parse tree produced by grParser#set_.
    def enterSet_(self, ctx:grParser.Set_Context):
        pass

    # Exit a parse tree produced by grParser#set_.
    def exitSet_(self, ctx:grParser.Set_Context):
        pass


    # Enter a parse tree produced by grParser#positive_set.
    def enterPositive_set(self, ctx:grParser.Positive_setContext):
        pass

    # Exit a parse tree produced by grParser#positive_set.
    def exitPositive_set(self, ctx:grParser.Positive_setContext):
        pass


    # Enter a parse tree produced by grParser#negative_set.
    def enterNegative_set(self, ctx:grParser.Negative_setContext):
        pass

    # Exit a parse tree produced by grParser#negative_set.
    def exitNegative_set(self, ctx:grParser.Negative_setContext):
        pass


    # Enter a parse tree produced by grParser#set_items.
    def enterSet_items(self, ctx:grParser.Set_itemsContext):
        pass

    # Exit a parse tree produced by grParser#set_items.
    def exitSet_items(self, ctx:grParser.Set_itemsContext):
        pass


    # Enter a parse tree produced by grParser#set_item.
    def enterSet_item(self, ctx:grParser.Set_itemContext):
        pass

    # Exit a parse tree produced by grParser#set_item.
    def exitSet_item(self, ctx:grParser.Set_itemContext):
        pass


    # Enter a parse tree produced by grParser#range_.
    def enterRange_(self, ctx:grParser.Range_Context):
        pass

    # Exit a parse tree produced by grParser#range_.
    def exitRange_(self, ctx:grParser.Range_Context):
        pass


    # Enter a parse tree produced by grParser#metachar.
    def enterMetachar(self, ctx:grParser.MetacharContext):
        pass

    # Exit a parse tree produced by grParser#metachar.
    def exitMetachar(self, ctx:grParser.MetacharContext):
        pass


    # Enter a parse tree produced by grParser#non_metachar.
    def enterNon_metachar(self, ctx:grParser.Non_metacharContext):
        pass

    # Exit a parse tree produced by grParser#non_metachar.
    def exitNon_metachar(self, ctx:grParser.Non_metacharContext):
        pass



del grParser