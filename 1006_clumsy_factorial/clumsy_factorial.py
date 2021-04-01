import operator


class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        N -= 1
        poistion = 0
        while N > 0:
            if poistion % 4 == 0:
                stack.append(stack.pop() * N)
            elif poistion % 4 == 1:
                stack.append(int(operator.truediv(stack.pop(), N)))
            elif poistion % 4 == 2:
                stack.append(N)
            else:
                stack.append(-N)
            poistion += 1
            N -= 1
        return sum(stack)
