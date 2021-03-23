# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.index = -1

        def dsf(obj: nestedList):
            for i in obj:
                if i.isInteger():
                    self.data.append(i)
                else:
                    dsf(i.getList())

        dsf(nestedList)

    def next(self) -> int:
        if self.hasNext():
            self.index += 1
            return self.data[self.index]
        else:
            return -1

    def hasNext(self) -> bool:
        return True if self.index < len(self.data) - 1 else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
