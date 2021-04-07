int removeDuplicates(int* nums, int numsSize){
    if (numsSize < 3) {
        return numsSize;
    }
    int slow = 2, fast = 2;
    while (fast < numsSize) {
        if (nums[slow - 2] != nums[fast]) {
            nums[slow++] = nums[fast];
        }
        fast += 1;
    }
    return slow;
}