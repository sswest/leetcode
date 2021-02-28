from unittest import TestCase
from merge_k_sorted_lists import *


class TestSolution(TestCase):
    def test_merge_klists(self):
        i = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lists = [list_to_node(r) for r in i]
        r = Solution().mergeKLists(lists)
        self.assertEqual(node_to_list(r), [1, 1, 2, 3, 4, 4, 5, 6])
