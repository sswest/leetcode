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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(val=None, next=head)
        prev, cur = dummy, head
        while cur:
            if cur.val == prev.val:
                cur = cur.next
                prev.next = cur
                continue
            prev, cur = cur, cur.next
        return dummy.next
