from unittest import TestCase
from add_two_numbers import Solution, ListNode


class TestSolution(TestCase):
    @staticmethod
    def create_link(number: int) -> ListNode:
        dummy = cur = ListNode()
        for n in (str(number)[::-1]):
            cur.next = ListNode(int(n))
            cur = cur.next
        return dummy.next

    def test_add_two_numbers(self):
        l1 = self.create_link(342)
        l2 = self.create_link(465)
        out = self.create_link(807)
        test_out = Solution().addTwoNumbers(l1, l2)
        while out:
            self.assertEqual(out.val, test_out.val)
            out = out.next
            test_out = test_out.next

