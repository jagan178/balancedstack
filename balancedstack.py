class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
def is_balanced(expression):
    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return "Not Balanced"
    return "Balanced" if stack.is_empty() else "Not Balanced"
def check_multiple_expressions(expressions):
    results = []
    for expression in expressions:
        results.append(is_balanced(expression))
    return results
if __name__ == "__main__":
    n = int(input())      
    expressions = []
    for _ in range(n):
        expression = input().strip()
        expressions.append(expression)
    results = check_multiple_expressions(expressions)
    for result in results:
        print(result)
