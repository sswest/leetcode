bool find132pattern(int* nums, int numsSize){
    int i, j, k;
    if (numsSize < 3) {
        return false;
    }
    i = 0;
    for (j=1; j < numsSize -1 ; j++) {
        if (nums[j] < nums[i]) {
            i = j;
        } else {
            for (k = j+1; k < numsSize; k++) {
                if (nums[j] > nums[k] && nums[k] > nums[i]) {
                    return true;
                }
            }
        }
    }
    return false;
}