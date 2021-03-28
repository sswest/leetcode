# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        self.index = -1

        def foo(node: TreeNode):
            # 中序遍历
            if not node:
                return
            foo(node.left)
            self.data.append(node.val)
            foo(node.right)

        foo(root)

    def next(self) -> int:
        if self.hasNext():
            self.index += 1
            return self.data[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.data) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
