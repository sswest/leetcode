/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swap(ListNode node) {
        if (node == null || node.next == null) {
            return node;
        }
        ListNode tmp = node.next;
        node.next = swap(tmp.next);
        tmp.next = node;
        return tmp;
    }

    public ListNode swapPairs(ListNode head) {
        return swap(head);
    }
}