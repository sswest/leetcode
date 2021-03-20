from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                if i == '+':
                    stack.append(stack.pop() + stack.pop())
                elif i == '-':
                    n1 = stack.pop()
                    stack.append(stack.pop() - n1)
                elif i == '*':
                    stack.append(stack.pop() * stack.pop())
                elif i == '/':
                    n1 = stack.pop()
                    stack.append(int(stack.pop() / n1))
        return stack.pop()
