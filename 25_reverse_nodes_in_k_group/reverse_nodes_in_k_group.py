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
    def reverse(self, head: ListNode, tail: ListNode):
        """反转head->tail之间的链表"""
        if head == tail:
            return head
        node = self.reverse(head.next, tail)
        head.next.next = head
        head.next = None
        return node

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:  # 不足K个节点 不执行后续反转
                    return dummy.next
            next_node = tail.next  # 记录K区间末尾节点的后一个节点
            self.reverse(head, tail)  # 反转K个节点
            head, tail = tail, head  # 头尾指向反转
            pre.next = head  # 将K区间上一个节点指向反转后的头结点
            tail.next = next_node  # 将反转后的尾节点指向下一个节点
            pre = tail  # 移动K个位置
            head = tail.next  # 更改头结点位置

        return dummy.next

