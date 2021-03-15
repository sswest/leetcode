from unittest import TestCase
from binary_tree_postorder_traversal import Solution, TreeNode


class TestSolution(TestCase):
    def test_postorder_traversal(self):
        tree1 = TreeNode(1, right=TreeNode(2, TreeNode(3)))
        tree2 = TreeNode(1, right=TreeNode(2, TreeNode(3), TreeNode(4)))
        tree3 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                         TreeNode(5, TreeNode(6), TreeNode(7)))

        inputs = (tree1, tree2, tree3)
        outs = ([3, 2, 1], [3, 4, 2, 1], [3, 4, 2, 6, 7, 5, 1])
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().postorderTraversal(inp))
