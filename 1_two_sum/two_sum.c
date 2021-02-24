int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                *returnSize = 2;
                int *ret = malloc(2 * sizeof(int));
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}