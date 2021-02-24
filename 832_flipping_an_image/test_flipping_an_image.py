from unittest import TestCase
from .flipping_an_image import Solution


class TestSolution(TestCase):
    def test_flip_and_invert_image(self):
        inputs = (
            [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        )
        outs = (
            [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        )
        for i in range(len(inputs)):
            self.assertEqual(outs[i], Solution().flipAndInvertImage(inputs[i]))
