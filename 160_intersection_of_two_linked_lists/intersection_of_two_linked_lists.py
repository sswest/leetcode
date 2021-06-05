# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        # 注意，为了简化判断结果，假设节点值不重复
        return self.val == other.val


def list_to_node(nums: list) -> ListNode:
    """从列表构建链表"""
    dummy = ListNode(None)
    node = dummy
    for n in nums:
        node.next = ListNode(n)
        node = node.next
    return dummy.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = [], []
        while headA:
            l1.append(headA)
            if headA.next:
                headA = headA.next
            else:
                break
        while headB:
            l2.append(headB)
            if headB.next:
                headB = headB.next
            else:
                break
        ret = None
        while l1 and l2 and (va := l1.pop()) == (vb := l2.pop()):
            ret = va
            continue
        return ret
