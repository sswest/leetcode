/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        return height(root) != -1;
    }

    int height(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int l_h = height(node.left);
        int r_h = height(node.right);
        if (l_h == -1 || r_h == -1 ||  Math.abs(l_h - r_h) > 1) {
            return -1;
        } else {
            return Math.max(l_h, r_h) + 1;
        }
    }
}