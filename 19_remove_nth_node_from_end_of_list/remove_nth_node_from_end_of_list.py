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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        _head, dummy = head, ListNode(0, head)
        while _head:
            length += 1
            _head = _head.next
        target = length - n
        node = dummy
        while target:
            target -= 1
            node = node.next
        node.next = None if n == 1 else node.next.next
        return dummy.next

