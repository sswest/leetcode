from unittest import TestCase
from intersection_of_two_linked_lists import list_to_node, ListNode, Solution


class TestSolution(TestCase):
    def test_get_intersection_node(self):
        inputs = (
            (list_to_node([0, 9, 1, 2, 4]), list_to_node([3, 2, 4])),
        )
        outs = (
            ListNode(2),
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().getIntersectionNode(*inp))
