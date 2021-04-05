class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp = new int[m + n];
        int i = 0, j = 0;
        while (i + j < m + n) {
            if (j == n) {
                tmp[i + j] = nums1[i++];
                continue;
            }
            if (i == m) {
                tmp[i + j] = nums2[j++];
                continue;
            }

            if (nums2[j] < nums1[i]) {
                tmp[i + j] = nums2[j++];
            } else {
                tmp[i + j] = nums1[i++];
            }
        }
        for (int p = 0; p < m + n; p++) {
            nums1[p] = tmp[p];
        }
    }
}