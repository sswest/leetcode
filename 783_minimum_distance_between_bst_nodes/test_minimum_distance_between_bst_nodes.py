from unittest import TestCase
from minimum_distance_between_bst_nodes import Solution, TreeNode


class TestSolution(TestCase):
    def test_min_diff_in_bst(self):
        inputs = (
            TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)),
            TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
        )
        outs = (1, 1)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().minDiffInBST(inp))
