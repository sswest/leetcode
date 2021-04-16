import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private void prevIter(TreeNode node, ArrayList<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.val);
        prevIter(node.left, result);
        prevIter(node.right, result);
    }

    public int minDiffInBST(TreeNode root) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        prevIter(root, arr);
        Collections.sort(arr);
        int ans = arr.get(1) - arr.get(0);
        for (int i = 2; i < arr.size(); i ++) {
            ans = arr.get(i) - arr.get(i-1) < ans ? arr.get(i) - arr.get(i-1) : ans;
        }
        return ans;
    }
}