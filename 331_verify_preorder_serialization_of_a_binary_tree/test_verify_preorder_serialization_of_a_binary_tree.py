from unittest import TestCase
from verify_preorder_serialization_of_a_binary_tree import Solution


class TestSolution(TestCase):
    def test_is_valid_serialization(self):
        inputs = (
            "9,3,4,#,#,1,#,#,#,2,#,6,#,#",
            "1,#",
            "9,#,#,1"
        )
        outs = (False, False, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isValidSerialization(inp))
