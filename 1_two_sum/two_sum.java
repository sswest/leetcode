import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (hash.get(target - nums[i]) != null) {
                int arr[] = {i, hash.get(target - nums[i])};
                return arr;
            }
            hash.put(nums[i], i);
        }
        return null;
    }
}