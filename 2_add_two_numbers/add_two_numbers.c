/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2) {
    struct ListNode dummy = {0, NULL};
    struct ListNode *p = &dummy;
    struct ListNode *cur = p;
    int flag = 0;
    while (l1 != NULL || l2 != NULL || flag == 1) {
        if (l1 == NULL) {
            l1 = malloc(sizeof(struct ListNode));
            l1->val = 0;
            l1->next = NULL;
        }
        if (l2 == NULL) {
            l2 = malloc(sizeof(struct ListNode));
            l2->val = 0;
            l2->next = NULL;
        }
        cur->next = malloc(sizeof(struct ListNode));
        cur->next->val = (l1->val + l2->val + flag) % 10;
        cur->next->next = NULL;
        flag = (l1->val + l2->val + flag) / 10;
        cur = cur->next;
        l1 = l1->next;
        l2 = l2->next;
    }
    return p->next;
}