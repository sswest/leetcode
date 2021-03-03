/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize){
    *returnSize = num + 1;
    int *result = malloc(sizeof(int) * (num + 1));
    result[0] = 0;
    for (int i = 1; i <= num; i++) {
        result[i] = result[i >> 1] + i % 2;
    }
    return result;
}