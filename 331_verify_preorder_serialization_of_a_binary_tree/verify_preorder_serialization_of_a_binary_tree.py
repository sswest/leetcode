class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        preorders = preorder.split(',')
        n = len(preorders)
        for s in preorders:
            n -= 1
            if s == '#':
                slots -= 1
            else:
                slots += 1
            if slots == 0 and n > 0:
                return False
        return slots == 0
