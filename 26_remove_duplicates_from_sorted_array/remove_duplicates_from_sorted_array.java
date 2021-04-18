class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        int i = 0, j = 0;
        while (j < nums.length) {
            if (nums[j] != nums[i]) {
                nums[++i] = nums[j];
            }
            j++;
        }
        return i + 1;
    }
}