## 解题思路

### 递归

将矩阵视为一层一层包裹的矩形，每次将矩阵最外层的数据加入到结果数组中，然后递归矩阵第二层


### 模拟移动

观察可以得出移动方向有且仅有四种情况，且变化轨迹一直，可以建立一个方向数组，通过判断当前位置来判断是否需要改变方向