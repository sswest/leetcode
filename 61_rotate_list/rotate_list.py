# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_node(nums: list) -> ListNode:
    """从列表构建链表"""
    dummy = ListNode()
    node = dummy
    for n in nums:
        node.next = ListNode(n)
        node = node.next
    return dummy.next


def node_to_list(head: ListNode) -> list:
    """从链表转列表"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        size = 0
        tail, cur = ListNode(next=head), head
        while cur:
            size += 1
            cur = cur.next
            tail = tail.next
        if size < 2:
            return head
        if k >= size:
            k %= size
        if k == 0:
            return head
        prev, cur = ListNode(next=head), head
        while 0 < k < size:
            k += 1
            cur = cur.next
            prev = prev.next
        prev.next = None
        tail.next = head
        return cur
