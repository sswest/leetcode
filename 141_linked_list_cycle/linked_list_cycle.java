/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode s = head, q = head;
        while (s != null && q != null) {
            s = s.next;
            if (q.next == null) {
                break;
            }
            q = q.next.next;
            if (s == q) {
                return true;
            }
        }
        return false;
    }
}