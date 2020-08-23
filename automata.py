

class state():
    _count = 0

    def __init__(self, isEnd):
        self.name = 'Q'+str(state._count)
        state._count += 1
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


def addNextState(initialState, nextStates, visited, recursive): #Abstrai as transições vazias
    if (len(initialState.nullTransitions)):
        nextStates.append(initialState)
        for st in initialState.nullTransitions:
            if not st in visited:
                visited.append(st)
                addNextState(st, nextStates, visited, recursive+1)
        if not recursive:
            print("{} - {} -> [{}]".format(initialState.name, 'ε', ', '.join([vs.name for vs in nextStates])))
    else:
        nextStates.append(initialState)


def match(nfa, word):
    currentStates = []
    addNextState(nfa[0], currentStates, [], 0)

    for token in word:
        nextStates = []

        for currentState in currentStates:
            nextState = currentState.transitions[token] if token in currentState.transitions else None
            if (nextState):
                print("{} - {} -> {}".format(currentState.name, token, nextState.name))
                addNextState(nextState, nextStates, [], 0)
        currentStates = nextStates

    return True if any([x.isEnd for x in currentStates]) else False