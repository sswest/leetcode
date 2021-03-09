from unittest import TestCase
from remove_all_adjacent_duplicates_in_string import Solution


class TestSolution(TestCase):
    def test_remove_duplicates(self):
        inputs = ('abbaca', "abbbaca")
        outs = ('ca', "abaca")
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().removeDuplicates(inp), out)

