from unittest import TestCase
from binary_tree_zigzag_level_order_traversal import Solution, TreeNode


class TestSolution(TestCase):
    def test_zigzag_level_order(self):
        root = TreeNode(3, left=TreeNode(9, TreeNode(31), TreeNode(24)), right=TreeNode(20, TreeNode(15), TreeNode(7)))
        out = [[3], [20, 9], [31, 24, 15, 7]]
        self.assertEqual(Solution().zigzagLevelOrder(root), out)
