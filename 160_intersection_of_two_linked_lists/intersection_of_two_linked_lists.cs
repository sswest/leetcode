/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        Stack<ListNode> l1 = new Stack<ListNode>();
        Stack<ListNode> l2 = new Stack<ListNode>();
        while (headA != null)
        {
            l1.Push(headA);
            headA = headA.next;
        }
        while (headB != null)
        {
            l2.Push(headB);
            headB = headB.next;
        }

        ListNode ret = null;
        while (l1.Count() > 0 && l2.Count() > 0)
        {
            ListNode tmp = l1.Pop();
            if (tmp == l2.Pop())
                ret = tmp;
            else
                break;
        }
        return ret;
    }
}