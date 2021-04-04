# Definition for a binary tree node.
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = Queue()
        queue.put(root)
        ans = []
        direction = 1
        while not queue.empty():
            # 处理一层的每一个节点
            size = queue.qsize()
            tmp = []
            while size > 0:
                node = queue.get()
                tmp.append(node.val)

                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)

                size -= 1
            if tmp:
                if direction < 0:
                    tmp = tmp[::-1]
                ans.append(tmp)
            direction *= - 1
        return ans


if __name__ == '__main__':
    root = TreeNode(3, left=TreeNode(9, TreeNode(31), TreeNode(24)), right=TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().zigzagLevelOrder(root))