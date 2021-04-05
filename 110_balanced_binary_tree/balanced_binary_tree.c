/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b) {
    return a > b ? a : b;
}

int height(struct TreeNode* node) {
    if (node == NULL) {
        return 0;
    }
    int l_h = height(node->left);
    int r_h = height(node->right);
    if (l_h == -1 || r_h == -1 ||  abs(l_h - r_h) > 1) {
        return -1;
    } else {
        return max(l_h, r_h) + 1;
    }
}

bool isBalanced(struct TreeNode* root){
    return height(root) != -1;
}
