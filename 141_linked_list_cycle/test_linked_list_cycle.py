from unittest import TestCase
from linked_list_cycle import ListNode, Solution


class TestSolution(TestCase):
    def test_has_cycle(self):
        inputs = (
            ([3, 2, 0, -4], 1),
            ([1, 2], 0),
            ([1], -1)
        )
        outs = (True, True, False)
        for inp, out in zip(inputs, outs):
            ln = ListNode.from_list(*inp)
            self.assertEqual(Solution().hasCycle(ln), out)

