int search(int* nums, int numsSize, int target){
    int k = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] > nums[i]) {
            k = i;
            break;
        }
    }
    int nums2[numsSize];
    for (int i = 0; i < numsSize; i++) {
        if (i < numsSize - k) {
            nums2[i] = nums[k+i];
        } else {
            nums2[i] = nums[i - numsSize + k];
        }
    }
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (nums2[mid] == target) {
            int ans = mid + k;
            if (ans > numsSize - 1) {
                ans %= numsSize;
            }
            return ans;
        } else if(nums2[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}