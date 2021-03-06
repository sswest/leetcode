import java.util.Stack;
import java.util.HashMap;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums2.length; i++) {
            while (!stack.empty() && nums2[i] > nums2[stack.peek()])
                map.put(nums2[stack.pop()], nums2[i]);
            stack.push(i);
        }
        int[] ans = new int[nums1.length];
        for (int i = 0; i< nums1.length; i++) {
            ans[i] = map.containsKey(nums1[i]) ? map.get(nums1[i]) : -1;
        }
        return ans;
    }
}