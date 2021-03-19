## 解题思路

根据`left`找到`pre`节点，根据`rigth`找到`tail`节点，`left`到`right`之间的反转可以使用递归思路，参考[25-反转连续k个链表](https://github.com/sswest/leetcode/tree/master/25_reverse_nodes_in_k_group)

反转后 重新将 `pre`、`tail`节点拼接好
