// Generated from e:\Faculdade\7 sem\CMP\t2\RegEx-Parser\gr.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class grParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39;
	public static final int
		RULE_re = 0, RULE_union = 1, RULE_simple_re = 2, RULE_concat = 3, RULE_basic_re = 4, 
		RULE_star = 5, RULE_plus = 6, RULE_group = 7, RULE_any_ = 8, RULE_eos = 9, 
		RULE_char_ = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"re", "union", "simple_re", "concat", "basic_re", "star", "plus", "group", 
			"any_", "eos", "char_"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'|'", "'*'", "'+'", "'('", "')'", "'.'", "'$'", "'a'", "'b'", 
			"'c'", "'d'", "'e'", "'f'", "'g'", "'h'", "'i'", "'j'", "'k'", "'l'", 
			"'m'", "'n'", "'o'", "'p'", "'q'", "'r'", "'s'", "'t'", "'u'", "'v'", 
			"'w'", "'x'", "'y'", "'z'", "'\\'", "'['", "']'", "'^'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ReContext extends ParserRuleContext {
		public UnionContext union() {
			return getRuleContext(UnionContext.class,0);
		}
		public Simple_reContext simple_re() {
			return getRuleContext(Simple_reContext.class,0);
		}
		public ReContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_re; }
	}

	public final ReContext re() throws RecognitionException {
		ReContext _localctx = new ReContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_re);
		try {
			setState(24);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				union();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(23);
				simple_re();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnionContext extends ParserRuleContext {
		public Simple_reContext simple_re() {
			return getRuleContext(Simple_reContext.class,0);
		}
		public ReContext re() {
			return getRuleContext(ReContext.class,0);
		}
		public UnionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_union; }
	}

	public final UnionContext union() throws RecognitionException {
		UnionContext _localctx = new UnionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_union);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			simple_re();
			setState(27);
			match(T__0);
			setState(28);
			re();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_reContext extends ParserRuleContext {
		public ConcatContext concat() {
			return getRuleContext(ConcatContext.class,0);
		}
		public Basic_reContext basic_re() {
			return getRuleContext(Basic_reContext.class,0);
		}
		public Simple_reContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_re; }
	}

	public final Simple_reContext simple_re() throws RecognitionException {
		Simple_reContext _localctx = new Simple_reContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_simple_re);
		try {
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				concat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				basic_re();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConcatContext extends ParserRuleContext {
		public Basic_reContext basic_re() {
			return getRuleContext(Basic_reContext.class,0);
		}
		public Simple_reContext simple_re() {
			return getRuleContext(Simple_reContext.class,0);
		}
		public ConcatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concat; }
	}

	public final ConcatContext concat() throws RecognitionException {
		ConcatContext _localctx = new ConcatContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_concat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			basic_re();
			setState(35);
			simple_re();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Basic_reContext extends ParserRuleContext {
		public StarContext star() {
			return getRuleContext(StarContext.class,0);
		}
		public PlusContext plus() {
			return getRuleContext(PlusContext.class,0);
		}
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Any_Context any_() {
			return getRuleContext(Any_Context.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public Char_Context char_() {
			return getRuleContext(Char_Context.class,0);
		}
		public Basic_reContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_basic_re; }
	}

	public final Basic_reContext basic_re() throws RecognitionException {
		Basic_reContext _localctx = new Basic_reContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_basic_re);
		try {
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				star();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				plus();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(43);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__3:
					{
					setState(39);
					group();
					}
					break;
				case T__5:
					{
					setState(40);
					any_();
					}
					break;
				case T__6:
					{
					setState(41);
					eos();
					}
					break;
				case T__7:
				case T__8:
				case T__9:
				case T__10:
				case T__11:
				case T__12:
				case T__13:
				case T__14:
				case T__15:
				case T__16:
				case T__17:
				case T__18:
				case T__19:
				case T__20:
				case T__21:
				case T__22:
				case T__23:
				case T__24:
				case T__25:
				case T__26:
				case T__27:
				case T__28:
				case T__29:
				case T__30:
				case T__31:
				case T__32:
				case T__33:
					{
					setState(42);
					char_();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StarContext extends ParserRuleContext {
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Any_Context any_() {
			return getRuleContext(Any_Context.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public Char_Context char_() {
			return getRuleContext(Char_Context.class,0);
		}
		public StarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_star; }
	}

	public final StarContext star() throws RecognitionException {
		StarContext _localctx = new StarContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_star);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				{
				setState(47);
				group();
				}
				break;
			case T__5:
				{
				setState(48);
				any_();
				}
				break;
			case T__6:
				{
				setState(49);
				eos();
				}
				break;
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
				{
				setState(50);
				char_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(53);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PlusContext extends ParserRuleContext {
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Any_Context any_() {
			return getRuleContext(Any_Context.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public Char_Context char_() {
			return getRuleContext(Char_Context.class,0);
		}
		public PlusContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plus; }
	}

	public final PlusContext plus() throws RecognitionException {
		PlusContext _localctx = new PlusContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_plus);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				{
				setState(55);
				group();
				}
				break;
			case T__5:
				{
				setState(56);
				any_();
				}
				break;
			case T__6:
				{
				setState(57);
				eos();
				}
				break;
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
				{
				setState(58);
				char_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(61);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GroupContext extends ParserRuleContext {
		public ReContext re() {
			return getRuleContext(ReContext.class,0);
		}
		public GroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group; }
	}

	public final GroupContext group() throws RecognitionException {
		GroupContext _localctx = new GroupContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_group);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(T__3);
			setState(64);
			re();
			setState(65);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Any_Context extends ParserRuleContext {
		public Any_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_any_; }
	}

	public final Any_Context any_() throws RecognitionException {
		Any_Context _localctx = new Any_Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_any_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EosContext extends ParserRuleContext {
		public EosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eos; }
	}

	public final EosContext eos() throws RecognitionException {
		EosContext _localctx = new EosContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_eos);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Char_Context extends ParserRuleContext {
		public Char_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char_; }
	}

	public final Char_Context char_() throws RecognitionException {
		Char_Context _localctx = new Char_Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_char_);
		int _la;
		try {
			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				match(T__7);
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				match(T__8);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 3);
				{
				setState(73);
				match(T__9);
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 4);
				{
				setState(74);
				match(T__10);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 5);
				{
				setState(75);
				match(T__11);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 6);
				{
				setState(76);
				match(T__12);
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 7);
				{
				setState(77);
				match(T__13);
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 8);
				{
				setState(78);
				match(T__14);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 9);
				{
				setState(79);
				match(T__15);
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 10);
				{
				setState(80);
				match(T__16);
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 11);
				{
				setState(81);
				match(T__17);
				}
				break;
			case T__18:
				enterOuterAlt(_localctx, 12);
				{
				setState(82);
				match(T__18);
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 13);
				{
				setState(83);
				match(T__19);
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 14);
				{
				setState(84);
				match(T__20);
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 15);
				{
				setState(85);
				match(T__21);
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 16);
				{
				setState(86);
				match(T__22);
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 17);
				{
				setState(87);
				match(T__23);
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 18);
				{
				setState(88);
				match(T__24);
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 19);
				{
				setState(89);
				match(T__25);
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 20);
				{
				setState(90);
				match(T__26);
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 21);
				{
				setState(91);
				match(T__27);
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 22);
				{
				setState(92);
				match(T__28);
				}
				break;
			case T__29:
				enterOuterAlt(_localctx, 23);
				{
				setState(93);
				match(T__29);
				}
				break;
			case T__30:
				enterOuterAlt(_localctx, 24);
				{
				setState(94);
				match(T__30);
				}
				break;
			case T__31:
				enterOuterAlt(_localctx, 25);
				{
				setState(95);
				match(T__31);
				}
				break;
			case T__32:
				enterOuterAlt(_localctx, 26);
				{
				setState(96);
				match(T__32);
				}
				break;
			case T__33:
				enterOuterAlt(_localctx, 27);
				{
				setState(97);
				match(T__33);
				setState(98);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)h\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f"+
		"\t\f\3\2\3\2\5\2\33\n\2\3\3\3\3\3\3\3\3\3\4\3\4\5\4#\n\4\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\5\6.\n\6\5\6\60\n\6\3\7\3\7\3\7\3\7\5\7\66\n\7"+
		"\3\7\3\7\3\b\3\b\3\b\3\b\5\b>\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\ff\n\f\3\f\2\2\r\2"+
		"\4\6\b\n\f\16\20\22\24\26\2\3\4\2\3\t$)\2\u0083\2\32\3\2\2\2\4\34\3\2"+
		"\2\2\6\"\3\2\2\2\b$\3\2\2\2\n/\3\2\2\2\f\65\3\2\2\2\16=\3\2\2\2\20A\3"+
		"\2\2\2\22E\3\2\2\2\24G\3\2\2\2\26e\3\2\2\2\30\33\5\4\3\2\31\33\5\6\4\2"+
		"\32\30\3\2\2\2\32\31\3\2\2\2\33\3\3\2\2\2\34\35\5\6\4\2\35\36\7\3\2\2"+
		"\36\37\5\2\2\2\37\5\3\2\2\2 #\5\b\5\2!#\5\n\6\2\" \3\2\2\2\"!\3\2\2\2"+
		"#\7\3\2\2\2$%\5\n\6\2%&\5\6\4\2&\t\3\2\2\2\'\60\5\f\7\2(\60\5\16\b\2)"+
		".\5\20\t\2*.\5\22\n\2+.\5\24\13\2,.\5\26\f\2-)\3\2\2\2-*\3\2\2\2-+\3\2"+
		"\2\2-,\3\2\2\2.\60\3\2\2\2/\'\3\2\2\2/(\3\2\2\2/-\3\2\2\2\60\13\3\2\2"+
		"\2\61\66\5\20\t\2\62\66\5\22\n\2\63\66\5\24\13\2\64\66\5\26\f\2\65\61"+
		"\3\2\2\2\65\62\3\2\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2\678\7"+
		"\4\2\28\r\3\2\2\29>\5\20\t\2:>\5\22\n\2;>\5\24\13\2<>\5\26\f\2=9\3\2\2"+
		"\2=:\3\2\2\2=;\3\2\2\2=<\3\2\2\2>?\3\2\2\2?@\7\5\2\2@\17\3\2\2\2AB\7\6"+
		"\2\2BC\5\2\2\2CD\7\7\2\2D\21\3\2\2\2EF\7\b\2\2F\23\3\2\2\2GH\7\t\2\2H"+
		"\25\3\2\2\2If\7\n\2\2Jf\7\13\2\2Kf\7\f\2\2Lf\7\r\2\2Mf\7\16\2\2Nf\7\17"+
		"\2\2Of\7\20\2\2Pf\7\21\2\2Qf\7\22\2\2Rf\7\23\2\2Sf\7\24\2\2Tf\7\25\2\2"+
		"Uf\7\26\2\2Vf\7\27\2\2Wf\7\30\2\2Xf\7\31\2\2Yf\7\32\2\2Zf\7\33\2\2[f\7"+
		"\34\2\2\\f\7\35\2\2]f\7\36\2\2^f\7\37\2\2_f\7 \2\2`f\7!\2\2af\7\"\2\2"+
		"bf\7#\2\2cd\7$\2\2df\t\2\2\2eI\3\2\2\2eJ\3\2\2\2eK\3\2\2\2eL\3\2\2\2e"+
		"M\3\2\2\2eN\3\2\2\2eO\3\2\2\2eP\3\2\2\2eQ\3\2\2\2eR\3\2\2\2eS\3\2\2\2"+
		"eT\3\2\2\2eU\3\2\2\2eV\3\2\2\2eW\3\2\2\2eX\3\2\2\2eY\3\2\2\2eZ\3\2\2\2"+
		"e[\3\2\2\2e\\\3\2\2\2e]\3\2\2\2e^\3\2\2\2e_\3\2\2\2e`\3\2\2\2ea\3\2\2"+
		"\2eb\3\2\2\2ec\3\2\2\2f\27\3\2\2\2\t\32\"-/\65=e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}