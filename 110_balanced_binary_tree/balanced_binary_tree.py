# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            l_h = height(node.left)
            r_h = height(node.right)
            if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            else:
                return max(l_h, r_h) + 1

        return height(root) >= 0
