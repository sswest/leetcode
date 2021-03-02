from unittest import TestCase
from implement_strstr import Solution


class TestSolution(TestCase):
    def test_str_str(self):
        inputs = (
            ('aaaaa', 'bba'),
            ('hello', 'll'),
            ('mississippi', 'a')
        )
        outs = (-1, 2, -1)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().strStr(*inp))
