grammar gr;

re : union | simple_re ;
union : simple_re '|' re ;
simple_re : concat | basic_re ;
concat : basic_re simple_re ;
basic_re : star | plus | elementary_re ;
star : elementary_re '*' ;
plus : elementary_re '+' ;
elementary_re : group | any_ | eos | char_ ;
group : '(' re ')' ;
any_ : '.' ;
eos : '$' ;
char_ : non_metachar | '\\' metachar ;
metachar : '[' | ']' | '\\' | '.' | '^' | '$' | '*' | '+' | '{' | '}' | '|' | '(' | ')' ; 
non_metachar : 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' ; 

