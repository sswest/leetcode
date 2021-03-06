## 解题思路

### 有序后二分查找

和普通二分查找的区别在于，传入的数组不是有序的，题目中的数组是经过旋转后的数组

可以先将这个旋转数组重新排序，那么就能使用二分法了

由于旋转前数组是有序的，因此可以在O(n)的时间内将数组还原成有序数组

具体而言，先找到旋转位置`k`，在`k`处一定会有`nums[k - 1] > nums[k]`

然后重新构造一个有序数组`nums[k:] + nums[:k]`

有序数组二分查找的时间复杂度为O(logn)
