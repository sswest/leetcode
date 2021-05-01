from unittest import TestCase
from employee_importance import *


class TestSolution(TestCase):
    def test_get_importance(self):
        inputs = (
            ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1),
            ([[1, 2, [2]], [2, 3, []]], 2)
        )
        outs = (11, 3)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().getImportance([Employee(*arg) for arg in inp[0]], inp[1]))
