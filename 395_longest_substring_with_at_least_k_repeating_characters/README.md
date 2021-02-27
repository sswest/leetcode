## 解题思路

### 暴力破解法
最直观可以从头遍历所有子串，判断在满足条件下的最长。
```python
    res = 0
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            flag = False
            for c in set(s[i:j]):
                if s[i:j].count(c) < k:
                    flag = True
                    break
            if not flag:
                res = max(res, j-i)
```

### 分治递归法
观察发现，假如一个字符出现的次数少于K次，那么包含该字符的字符串一定不满足题目条件。

我们可以按这些少于K次的字符分割原字符串，将问题转换为求分割后的子字符串的最长子串（递归调用）

当一个子串的所有字符出现次数均大于等于K时，那么返回该字符串的长度（结束条件）

```python
for sp_char in set(s):
    if s.count(sp_char) < k:
        sub_strs = s.split(sp_char)
        return max(*[self.longestSubstring(sub_str, k) for sub_str in sub_strs])
return len(s)
```