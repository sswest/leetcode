from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        node = dummy
        while any(lists):
            min_node = ListNode(10 ** 4)
            index_ = 0
            for i, n in enumerate(lists):
                if n and n.val < min_node.val:
                    index_, min_node = i, n
            node.next = min_node
            node = node.next
            if not min_node.next:
                lists.pop(index_)
            else:
                lists[index_] = min_node.next
        return dummy.next
