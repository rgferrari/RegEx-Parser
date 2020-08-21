grammar gr;

re : union | simple_re ;
union : simple_re '|' re ;
simple_re : concat | basic_re ;
concat : basic_re simple_re ;
basic_re : star | plus | elementary_re ;
star : elementary_re '*' ;
plus : elementary_re '+' ;
elementary_re : group | any_ | eos | char | set_ ;
group : '(' re ')' ;
any_ : '.' ;
eos : '$' ;
char : non_metachar | '\\' metachar ;
set_ : positive_set | negative_set ;
positive_set : '[' set_items ']' ;
negative_set : '[^' set_items ']' ;
set_items : set_item | set_item set_items ;
set_item : range_ | char ;
range_ : char '-' char ;
metachar : '[' | ']' | '\\' | '.' | '^' | '$' | '*' | '+' | '{' | '}' | '|' | '(' | ')' ; 
non_metachar : ~('[' | ']' | '\\' | '.' | '^' | '$' | '*' | '+' | '{' | '}' | '|' | '(' | ')') ;