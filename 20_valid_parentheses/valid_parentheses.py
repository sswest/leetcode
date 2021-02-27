class Solution:
    def isValid(self, s: str) -> bool:
        left, right = '([{', '}])'
        total = left + right
        signed = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char not in total:
                return False
            if char in left:
                stack.append(char)
            else:
                if not stack:
                    return False
                if signed[char] != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True

