## 解题思路

### 方法一

对于一个整数x，通过位与运算`x & (x-1)`可以移除一个值为1的最小二进制位

```python
# x = 5
1 1 0
# x-1=4
1 0 0
# x & (x - 1)
1 0 0
# x & (x - 1) & (x - 2)
0 0 0
```

不断进行位与运算，最终会得到0，进行位与运算的次数就是二进制位为1的数量

### 方法二

对于一个正整数x

如果是偶数，最低位为0，此时右移一个单位，`x' = x // 2`，x的一比特数等于x'

如果是奇数，最低位为1，此时右移一个单位，`x' = x // 2`，x的一比特数等于x' + 1

总结上面的逻辑，也就是x的一比特位会等于x>>1比特位加上mod(x, 2)，也就是

`bit(x) = bit(x >> 1) + x % 2`