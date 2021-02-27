## 解题思路

思路和[15-三数之和](https://github.com/sswest/leetcode/tree/master/15_3sum) 差不多，通过排序+双指针实现时间复杂度O(N<sup>3</sup>)算法

具体实现时可以枝剪许多条件

* 在确定第一个数之后，如果 nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target，说明此时剩下的三个数无论取什么值，四数之和一定大于 target，因此退出第一重循环；
* 在确定第一个数之后，如果 nums[i]+nums[n-3]+nums[n-2]+nums[n-1]<target，说明此时剩下的三个数无论取什么值，四数之和一定小于 target，因此第一重循环直接进入下一轮，枚举 nums[i+1]nums[i+1]；
* 在确定前两个数之后，如果 nums[i]+nums[j]+nums[j+1]+nums[j+2]>target，说明此时剩下的两个数无论取什么值，四数之和一定大于 target，因此退出第二重循环；
* 在确定前两个数之后，如果 nums[i]+nums[j]+nums[n-2]+nums[n-1]<<target，说明此时剩下的两个数无论取什么值，四数之和一定小于 target，因此第二重循环直接进入下一轮，枚举 nums[j+1]nums[j+1]。
