from unittest import TestCase
from range_sum_of_bst import Solution, TreeNode


class TestSolution(TestCase):
    def test_back_order(self):
        inputs = (
            (TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, right=TreeNode(18))), 7, 15),
            (TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
                     TreeNode(15, TreeNode(13), TreeNode(18))), 6, 10)
        )
        outs = (32, 23)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().rangeSumBST(*inp))
