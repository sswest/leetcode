class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_list(nums: list, poi: int) -> 'ListNode':
        dummy = cur = ListNode(None)
        link = None
        for i, num in enumerate(nums):
            node = ListNode(num)
            cur.next = node
            cur = node
            if i == poi:
                link = node
        cur.next = link
        return dummy.next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s, q = head, head
        while s and q:
            s = s.next
            if not q.next:
                break
            q = q.next.next
            if s == q:
                return True
        return False
