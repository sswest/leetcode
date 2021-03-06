import java.util.Stack;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = -1;
        }
        for (int i = 0; i < 2 * n - 1; i++) {
            while (!stack.empty() && nums[i % n] > nums[stack.peek()])
                ans[stack.pop()] = nums[i % n];
            stack.push(i % n);
        }
        return ans;
    }
}