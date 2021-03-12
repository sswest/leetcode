class Solution:
    def reverseVowels(self, s: str) -> str:
        yy = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left] not in yy:
                left += 1
            if s[right] not in yy:
                right -= 1
            if s[left] in yy and s[right] in yy:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels('leetcode'))
