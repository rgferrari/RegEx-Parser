

class state():
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.transitions = {}
        self.nullTransitions = []


def addNullTransition(origin, destiny):
    origin.nullTransitions.append(destiny)


def addTransition(origin, destiny, token):
    origin.transitions[token] = destiny


def fromNull():
    start = state(False)
    end = state(True)
    addNullTransition(start, end)

    return [start, end]


def fromToken(symbol):
    start = state(False)
    end = state(True)
    addTransition(start, end, symbol)

    return [start, end]


def unionExpression(firstExp, secondExp):
    start = state(False)
    end = state(True)

    addNullTransition(start, firstExp[0])
    addNullTransition(start, secondExp[0])
    addNullTransition(end, firstExp[1])
    addNullTransition(end, secondExp[1])

    return [start, end]

    
def closureKleeneExpression(nfa):
    start = state(False)
    end = state(True)

    addNullTransition(start, nfa[0])
    addNullTransition(start, end)
    addNullTransition(nfa[1], nfa[0])
    addNullTransition(nfa[1], end)

    nfa[1].isEnd = False

    return [start, end]


def closurePlusExpression(nfa):
    start = state(False)
    end = state(True)

    addNullTransition(start, nfa[0])
    addNullTransition(nfa[1], nfa[0])
    addNullTransition(nfa[1], end)
    isEnd = False

    return [start, end]


def concatExpression(origin, destiny):
    addNullTransition(origin[1], destiny[0])
    origin[1].isEnd = False

    return [origin[0], destiny[1]]

def toNFA(postfixExp):
    if not postfixExp: # Se a regex for uma string vazia
        return fromNull() # Retorna um automato que identifica vazio

    stack = []

    print(postfixExp)

    for token in postfixExp:
        if (token == '*'):
            stack.append(closureKleeneExpression(stack.pop()))
        elif (token == "+"):
            stack.append(closurePlusExpression(stack.pop()))
        elif (token == '|'):
            right = stack.pop()
            left = stack.pop()
            stack.append(unionExpression(left, right))
        elif (token == '?') :
            right = stack.pop()
            left = stack.pop()
            stack.append(concatExpression(left, right))
        else:
            stack.append(fromToken(token))

    return stack.pop()