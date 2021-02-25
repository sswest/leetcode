from unittest import TestCase
from palindrome_number import Solution


class TestSolution(TestCase):
    def test_is_palindrome(self):
        inputs = (121, -121, 10, -101)
        outs = (True, False, False, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isPalindrome(inp))

