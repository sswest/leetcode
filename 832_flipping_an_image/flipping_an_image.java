class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int n = A.length;
        for (int i = 0; i< n ; i++) {
            int left=0, right=A[i].length - 1;
            while (left < right) {
                int tmp = A[i][left];
                A[i][left] = A[i][right] ^ 1;
                A[i][right] = tmp ^ 1;
                left++;
                right--;
            }
            if (left == right) {
                A[i][left] ^= 1;
            }
        }
        return A;
    }
}