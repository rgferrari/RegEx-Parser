re : union | simple_re
union : re '|' simple_re
simple_re : concatenation | basic_re
basic_re : star | plus | elementary_re
star : elementary_re '*'
plus : elementary_re '+'
elementary_re : group | any | eos | char | set
group : '(' re ')'
any : '.'
eos : '$'
char : any non metacharacter | '\' metacharacter
set : positive_set | negative_set
positive_set : '[' set_items ']'
negative_set : '[^' set_items ']'
set_items : set_item | set_item set_items
set_item : range | char
range : char '-' char


<RE>    ::=     <union> | <simple-RE>
<union>     ::= <RE> "|" <simple-RE>
<simple-RE>     ::=     <concatenation> | <basic-RE>
<concatenation>     ::= <simple-RE> <basic-RE>
<basic-RE>  ::= <star> | <plus> | <elementary-RE>
<star>  ::= <elementary-RE> "*"
<plus>  ::= <elementary-RE> "+"
<elementary-RE>     ::= <group> | <any> | <eos> | <char> | <set>
<group>     ::=     "(" <RE> ")"
<any>   ::=     "."
<eos>   ::=     "$"
<char>  ::=     any non metacharacter | "\" metacharacter
<set>   ::=     <positive-set> | <negative-set>
<positive-set>  ::=     "[" <set-items> "]"
<negative-set>  ::=     "[^" <set-items> "]"
<set-items>     ::=     <set-item> | <set-item> <set-items>
<set-items>     ::=     <range> | <char>
<range>     ::=     <char> "-" <char>