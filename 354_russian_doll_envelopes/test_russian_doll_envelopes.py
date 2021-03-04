from unittest import TestCase
from russian_doll_envelopes import Solution


class TestSolution(TestCase):
    def test_max_envelopes(self):
        inputs = (
            [[5, 4], [6, 4], [6, 7], [2, 3]],
            [[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
        )
        outs = (3, 3)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().maxEnvelopes(inp))
