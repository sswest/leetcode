from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归解法
        # ans = []
        # if not root:
        #     return ans
        # ans += self.postorderTraversal(root.left)
        # ans += self.postorderTraversal(root.right)
        # ans.append(root.val)
        #
        # return ans

        # 迭代解法
        if not root:
            return []

        ans = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans
