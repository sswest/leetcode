/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode * s = head, * q = head;
    while (s != NULL && q != NULL) {
        s = s->next;
        if (q->next == NULL) {
            break;
        }
        q = q->next->next;
        if (s == q) {
            return true;
        }
    }
    return false;
}
