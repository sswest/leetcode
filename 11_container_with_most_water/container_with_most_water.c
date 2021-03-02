int maxArea(int* height, int heightSize){
    int left=0, right=heightSize-1;
    int result = 0;
    while (left < right) {
        int area;

        if (height[left] < height[right]) {
            area = (right - left) * height[left];
            left++;
        } else {
            area = (right - left) * height[right];
            right--;
        }
        if (area > result) result=area;
    }
    return result;
}