class Solution:
    def calculate(self, s):
        stack = []
        sign = '+'
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if i == len(s) - 1 or c in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                sign = c
                num = 0
        return sum(stack)
