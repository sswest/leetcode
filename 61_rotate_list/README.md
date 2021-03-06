## 解题思路

将链表旋转K个位置 实际上只需要链表中倒数第k个节点放置在链表头 并将链表尾节点的next指向原链表头

首先通过一次遍历，获取整个链表的长度size，然后处理k

1. 如果链表长度大于旋转位置`size > k`，那么只需要找到原链表倒数第k个节点`Node(k)`、倒数k+1个节点`prev=Node(k+1)`和链表最后一个节点`tail`。
    
    倒数k+1个节点变成尾节点`prev.next = None`，原尾节点的下一个节点指向原头结点`tail.next = head`，此时倒数第k个节点就变成了链表头节点。

2. 如果链表长度小于等于旋转位置`size <= k`，意味着旋转超过一圈，此时实际上只需要旋转`k % size`个位置，令`k %= size`，再按第一种情况处理。