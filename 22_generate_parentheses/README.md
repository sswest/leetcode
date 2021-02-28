## 解题思路

### 回溯法
如果左括号数量不大于n，可以放一个左括号。如果右括号数量小于左括号的数量，可以放一个右括号。

```python
compose, result = [], []

def backtrack(left: int, right: int):
    if len(compose) == 2 * n:
        result.append(''.join(compose))
    else:
        if left < n:
            compose.append('(')
            backtrack(left + 1, right)
            compose.pop()
        if right < left:
            compose.append(')')
            backtrack(left, right + 1)
            compose.pop()
```

