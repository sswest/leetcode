int majorityElement(int* nums, int numsSize){
    int key = nums[0];
    int count = 0;
    for (size_t i = 0; i < numsSize; i++)
    {
        if(nums[i] == key) {
            count++;
        }
        else {
            count--;
        }
        if(count <= 0) {
            key = nums[i+1];
        }
    }
    return key;
}
