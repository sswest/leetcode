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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        p1, p2 = l1, l2
        while p1 or p2:
            if not p1:
                # todo 直接加p2
                node.next = p2
                p2 = p2.next
            elif not p2:
                node.next = p1
                p1 = p1.next
            else:
                if p1.val <= p2.val:
                    node.next = p1
                    p1 = p1.next
                else:
                    node.next = p2
                    p2 = p2.next
            node = node.next
        return dummy.next
