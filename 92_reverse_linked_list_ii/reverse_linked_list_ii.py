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
    def reverse(self, head: ListNode, tail: ListNode):
        """反转head->tail之间的链表"""
        if head == tail:
            return head
        node = self.reverse(head.next, tail)
        head.next.next = head
        head.next = None
        return node

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummpy, i = ListNode(next=head), 1
        pre = dummpy
        while i < left:
            i += 1
            pre = pre.next
        _tail = pre
        while i <= right:
            i += 1
            _tail = _tail.next
        _next = _tail.next  # 反转尾节点的下一个节点
        tail = pre.next  # 反转后的尾节点
        pre.next = self.reverse(pre.next, _tail)
        tail.next = _next  # 将反转后的尾节点绑定

        return dummpy.next
