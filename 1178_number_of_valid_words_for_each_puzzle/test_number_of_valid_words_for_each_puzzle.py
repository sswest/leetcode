from unittest import TestCase
from number_of_valid_words_for_each_puzzle import Solution


class TestSolution(TestCase):
    def test_find_num_of_valid_words(self):
        inputs = (
            (["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
             ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
             ),
        )
        outs = (
            [1, 1, 3, 2, 4, 0],
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().findNumOfValidWords(*inp))
