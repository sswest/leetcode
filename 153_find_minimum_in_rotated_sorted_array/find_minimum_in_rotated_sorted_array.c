int findMin(int* nums, int numsSize){
    int k = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] > nums[i]) {
            k = i;
            break;
        }
    }
    return nums[k];
}