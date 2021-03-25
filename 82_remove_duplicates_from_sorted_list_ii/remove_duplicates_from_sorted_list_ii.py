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
        table = dict()
        node = head
        while node:
            table[node.val] = table.get(node.val, 0) + 1
            node = node.next
        dummy = cur = ListNode()
        for k, v in table.items():
            if v == 1:
                cur.next = ListNode(k)
                cur = cur.next
        return dummy.next
