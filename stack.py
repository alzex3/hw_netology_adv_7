class Stack:
    data = []

    def is_empty(self):
        return False if self.data else True

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return None if self.is_empty() else self.data[-1]

    def size(self):
        return len(self.data)


def balance(data):
    for i in data:
        if i == ')' and stack.peek() == '(':
            stack.pop()
        elif i == ']' and stack.peek() == '[':
            stack.pop()
        elif i == '}' and stack.peek() == '{':
            stack.pop()
        else:
            stack.push(i)
    if stack.size():
        print('Несбалансированно')
    else:
        print('Сбалансированно')


stack = Stack()

arr = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]
for i in arr:
    balance(i)
