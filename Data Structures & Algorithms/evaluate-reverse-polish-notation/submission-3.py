class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a+b
        def subtract(a, b):
            return a - b
        def multiply(a, b):
            return a*b
        def divide(a, b):
            return int(a/b)

        operators = {'+' : add, '-':subtract, '*':multiply, '/':divide}
        stack = []
        for t in tokens:
            if t not in operators.keys():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operators[t](a, b)
                stack.append(result)

        return stack.pop()

