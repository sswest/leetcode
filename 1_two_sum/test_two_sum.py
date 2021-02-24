from unittest import TestCase
from .two_sum import Solution


class TestSolution(TestCase):
    def test_two_sum(self):
        inputs = (
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6)
        )
        outs = (
            [0, 1], [1, 2], [0, 1]
        )
        for index, _input in enumerate(inputs):
            self.assertEqual(sorted(Solution().twoSum(*_input)), sorted(outs[index]))

