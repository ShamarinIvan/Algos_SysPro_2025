numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

def precedence(op):
    if op in ('(', ')'):
        return 10
    elif op in ('!', '~'):
        return 9
    elif op == '**':
        return 8
    elif op in ('*', '/', '%'):
        return 7
    elif op in ('+', '-'):
        return 6
    elif op in ('<<', '>>'):
        return 5
    elif op == '&':
        return 4
    elif op in '^':
        return 3
    elif op == '|':
        return 2
    elif op == '&&':
        return 1
    elif op == '||':
        return 0

def infix_to_polish(raw):
    output = ""
    symbols = raw.split()
    n = len(symbols)
    stack = Stack()
    for i in range(n):
        s = symbols[i]
        if s in numbers:
            output += s + " "
        elif s == '(':
            stack.push(s)
        elif s == ')':
            while not(stack.is_empty()) and stack.peek() != '(':
                output += stack.pop() + " "
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != '(' and (precedence(stack.peek()) > precedence(s) or (precedence(stack.peek()) == precedence(s) and stack.peek() != "**")):
                output += stack.pop() + " "
            stack.push(s)
    while not(stack.is_empty()):
        output += stack.pop() + " "
    return output
print(infix_to_polish("( 3 ** 4 ) ** 2"))

