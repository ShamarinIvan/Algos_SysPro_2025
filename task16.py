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
    precedence_map = {
        '(': 10, ')': 10,
        '!': 9, '~': 9,
        '**': 8,
        '*': 7, '/': 7, '%': 7,
        '+': 6, '-': 6,
        '<<': 5, '>>': 5,
        '&': 4,
        '^': 3,
        '|': 2,
        '&&': 1,
        '||': 0
    }
    return precedence_map[op]

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
    return output.strip()

test_cases = [
    ("3 + 4", "3 4 +"),
    ("3 * 4 + 2", "3 4 * 2 +"),
    ("3 + 4 * 2", "3 4 2 * +"),
    ("( 3 + 4 ) * 2", "3 4 + 2 *"),
    ("3 + 4 * 2 / ( 1 - 5 )", "3 4 2 * 1 5 - / +"),
    ("3 ** 4", "3 4 **"),
    ("( 3 ** 4 ) ** 2", "3 4 ** 2 **"),
    ("3 + 4 * 2 / ( 1 - 5 ) ** 2", "3 4 2 * 1 5 - 2 ** / +"),
    ("~ 3 + 4", "3 ~ 4 +"),
    ("3 + 4 * 2 << 1", "3 4 2 * + 1 <<"),
    ("3 && 4 || 2", "3 4 && 2 ||"),
    ("3 * 4 + 2 & 5", "3 4 * 2 + 5 &"),
    ("3 + 4 % 2 ^ 1", "3 4 2 % + 1 ^"),
]

for infix, expected in test_cases:
    result = infix_to_polish(infix)
    print(f"Вход: {infix: <30} Ожидается: {expected: <30} Получено: {result}",
          "OK" if result == expected else "NOT OK")
