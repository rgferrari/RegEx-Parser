import sys
from enum import Enum

precedence = {
    '|': 0,
    '?': 1,
    '*': 2,
    '+': 2
} 

def regexToPostfix(regex):
    postfix = []
    stack = []
    whileOn = True

    regex = concatCharAdd(regex)

    for i in range(len(regex)):
        if isOperator(regex[i]):
            while stack and stack[len(stack)-1] != '(' and precedence[stack[len(stack)-1]] >= precedence[regex[i]]:
                postfix.append(stack.pop())
            stack.append(regex[i])
        elif regex[i] == '(' or regex[i] == ')':
            if regex[i] == '(':
                stack.append(regex[i])
            else:
                while (stack[len(stack)-1] != '('):
                    postfix.append(stack.pop())
                stack.pop()
        else:
            postfix.append(regex[i])

    while (stack):
        postfix.append(stack.pop())

    return postfix


def isOperator(char):
    if char == '*' or char == '|' or char == '+' or char == '?':
        return True
    else:
        return False


def concatCharAdd(regex):
    regexWConcat = []
    for i in range(len(regex)):
        regexWConcat.append(regex[i])

        if regex[i] == '(' or regex[i] == '|':
            continue
        
        if i < len(regex)-1:
            if regex[i+1] == '*' or regex[i+1] == '+' or regex[i+1] == '|' or regex[i+1] == ')':
                continue

            regexWConcat.append('?')
    
    return regexWConcat



#a*b*
#a*?b*


#a(a|b)*b
#a?(a|b)*?b

#a((a|b)|a)b*
#a?((a|b)|a)?b*



# ignorar (), * +, ?(concat character), |

# class grValidator():
