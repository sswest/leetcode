int removeElement(int* nums, int numsSize, int val){
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == val) {
            continue;
        }
        nums[j] = nums[i];
        j++;
    }
    return j;
}