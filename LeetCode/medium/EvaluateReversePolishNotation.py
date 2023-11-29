class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')
        for index in tokens:
            if index not in operators:
                stack.append(index)
                continue
            a = int(stack.pop())
            b = int(stack.pop())
            if index == '+':
                stack.append(int(a + b))
            elif index == '*':
                stack.append(int(a * b))
            elif index == '-':
                stack.append(int(b - a))
            elif index == '/':
                stack.append(int(b / a))
        return int(stack[0])
    
