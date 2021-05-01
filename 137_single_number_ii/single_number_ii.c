struct HashTable {
    int key;
    int val;
    UT_hash_handle hh;
};

int singleNumber(int* nums, int numsSize){
    struct HashTable* hashTable = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct HashTable* tmp;
        HASH_FIND_INT(hashTable, &nums[i], tmp);
        if (tmp == NULL) {
            tmp = malloc(sizeof(struct HashTable));
            tmp->key = nums[i];
            tmp->val = 1;
            HASH_ADD_INT(hashTable, key, tmp);
        } else {
            tmp->val++;
        }
    }
    struct HashTable *iter, *tmp;
    HASH_ITER(hh, hashTable, iter, tmp) {
        if (iter->val == 1) {
            return iter->key;
        }
    }
    return -1;
}