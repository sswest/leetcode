class Solution {
    public boolean find132pattern(int[] nums) {
        int i, j, k, n = nums.length;
        if (n < 3) {
            return false;
        }
        i = 0;
        for (j=1; j < n -1 ; j++) {
            if (nums[j] < nums[i]) {
                i = j;
            } else {
                for (k = j+1; k < n; k++) {
                    if (nums[j] > nums[k] && nums[k] > nums[i]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}