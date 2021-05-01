from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance, target = dict(), None
        for employee in employees:
            importance[employee.id] = employee
            if employee.id == id:
                target = employee
        queue = target.subordinates
        ans = target.importance
        while queue:
            _queue = []
            while queue:
                ep = importance[queue.pop()]
                ans += ep.importance
                _queue.extend(ep.subordinates)
            queue = _queue

        return ans
