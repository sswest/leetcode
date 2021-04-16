# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def iter(self, root: TreeNode, result: list):
        if not root:
            return
        result.append(root.val)
        self.iter(root.left, result)
        self.iter(root.right, result)

    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        self.iter(root, values)
        values.sort()
        ans = values[1] - values[0]
        for i in range(2, len(values)):
            ans = ans if values[i] - values[i - 1] > ans else values[i] - values[i - 1]
        return ans


if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    print(Solution().minDiffInBST(tree))
