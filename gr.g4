grammar gr;

re : union | simple_re ;
union : re '|' simple_re ;
simple_re : concatenation | basic_re ;
basic_re : star | plus | elementary_re ;
star : elementary_re '*' ;
plus : elementary_re '+' ;
elementary_re : group | any | eos | char | set ;
group : '(' re ')' ;
any : '.' ;
eos : '$' ;
char : non_metachar | '\' metachar ;
set : positive_set | negative_set ;
positive_set : '[' set_items ']' ;
negative_set : '[^' set_items ']' ;
set_items : set_item | set_item set_items ;
set_item : range | char ;
range : char '-' char ;

metachar : '[' | ']' | '\' | '.' | '^' | '$' | '*' | '+' | '{' | '}' | '|' | '(' | ')' ; 
non_metachar : ~metachar ;