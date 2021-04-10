class Solution {
    public int findMin(int[] nums) {
        int k = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) {
                k = i;
                break;
            }
        }
        return nums[k];
    }
}