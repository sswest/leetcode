from unittest import TestCase
from binary_tree_level_order_traversal import Solution, TreeNode


class TestSolution(TestCase):
    def test_level_order(self):
        tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        inputs = (tree1, )
        outs = ([[3], [9, 20], [15, 7]], )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().levelOrder(inp))
