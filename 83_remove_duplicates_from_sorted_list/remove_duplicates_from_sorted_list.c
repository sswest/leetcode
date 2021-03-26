/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    struct ListNode *prev = dummy, *cur=head;
    dummy->val = -101;
    dummy->next = head;
    while (cur) {
        if (prev->val == cur->val) {
            prev->next = cur->next;
        } else {
            prev = cur;
        }
        cur = cur->next;
    }
    return dummy->next;
}