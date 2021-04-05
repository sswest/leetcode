void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int tmp[m + n];
    int i = 0, j = 0;
    while (i + j < m + n) {
        if (j == n) {
            tmp[i + j] = nums1[i];
            i++;
            continue;
        }
        if (i == m) {
            tmp[i + j] = nums2[j];
            j++;
            continue;
        }

        if (nums2[j] < nums1[i]) {
            tmp[i + j] = nums2[j];
            j++;
        } else {
            tmp[i+ j] = nums1[i];
            i++;
        }
    }
    for (int p = 0; p < m + n; p++) {
        nums1[p] = tmp[p];
    }
}