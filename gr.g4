grammar gr;

re : union | simple_re ;
union : simple_re '|' re ;
simple_re : concat | basic_re ;
concat : basic_re simple_re ;
basic_re : star | plus | (group | any_ | eos | char_ ) ;
star : (group | any_ | eos | char_ ) '*' ;
plus : (group | any_ | eos | char_ ) '+' ;
group : '(' re ')' ;
any_ : '.' ;
eos : '$' ;
char_ : 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '\\' ('[' | ']' | '\\' | '.' | '^' | '$' | '*' | '+' | '{' | '}' | '|' | '(' | ')') | 'E';

