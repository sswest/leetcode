/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    int ans[300];
    int size = 0;
    struct ListNode* node;
    if (head == NULL) {
        return head;
    } else {
        ans[size++] = head->val;
    }
    node = head->next;
    while (node) {
        if (size > 0 && node->val == ans[size - 1]) {
            while (node->next && node->next->val == node->val) {
                node = node->next;
            }
            size--;
        } else {
            ans[size++] = node->val;
        }
        node = node->next;
    }
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = NULL;
    node = dummy;
    for (int i =0; i<size;i++) {
        struct ListNode* obj = malloc(sizeof(struct ListNode));
        obj->val = ans[i];
        obj->next = NULL;
        node->next = obj;
        node = obj;
    }
    return dummy->next;
}