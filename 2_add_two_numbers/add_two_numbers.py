# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cl1, cl2, flag = l1, l2, 0  # flag变量用于进位
        dummy = cur = ListNode()  # 虚拟头节点
        while cl1 or cl2 or flag:
            if not cl1:
                cl1 = ListNode()
            if not cl2:
                cl2 = ListNode()
            val, flag = (cl1.val + cl2.val + flag) % 10, (cl1.val + cl2.val + flag) // 10
            cur.next = ListNode(val)
            cur = cur.next
            cl1, cl2 = cl1.next, cl2.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    out = ListNode(7)
    out.next = ListNode(0)
    out.next.next = ListNode(8)
    test_out = Solution().addTwoNumbers(l1, l2)
    while out:
        assert out.val == test_out.val
        out = out.next
        test_out = test_out.next
