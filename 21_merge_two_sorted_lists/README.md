## 解题思路

### 迭代法
建立一个全新的链表，对l1和l2迭代，判断当前节点p1和p2的值，如果p1<=p2，则将p1追加到新链表尾部，并修改指向p1->p1.next，反之亦然。

时间复杂度O(n+m) n、m为l1,l2链表长度 空间复杂度O(1)

