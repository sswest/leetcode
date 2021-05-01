class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def back_order(self, node: TreeNode) -> list:
        ans = []
        if not node:
            return ans
        ans.extend(self.back_order(node.left))
        ans.extend(self.back_order(node.right))
        ans.append(node.val)
        return ans

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        node_val = self.back_order(root)
        ans = 0
        for val in node_val:
            if low <= val <= high:
                ans += val

        return ans
