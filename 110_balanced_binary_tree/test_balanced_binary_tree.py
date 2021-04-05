from unittest import TestCase
from balanced_binary_tree import Solution, TreeNode


class TestSolution(TestCase):
    def test_height(self):
        tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
        inputs = (tree1, tree2)
        outs = (True, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isBalanced(inp))
