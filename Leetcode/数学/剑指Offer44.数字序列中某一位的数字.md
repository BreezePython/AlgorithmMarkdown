# 12.整数转罗马数字
> https://leetcode-cn.com/problems/integer-to-roman/
> 
> 难度：中等
## 题目：

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

## 示例：

示例1:

输入: s = "abcabcbb"

输出: 3 

解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: s = "bbbbb"

输出: 1

解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: s = "pwwkew"

输出: 3

解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
    
示例 4:

输入: s = ""

输出: 0

## 分析：

这道题只需要关注left如何跳转即可。如果重复的数字出现在left之前忽略，否则了跳到该值的下一个位置

## 解题：

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n -= 9
        count = 1
        while True:
            num = 10 ** count * 9 * (count + 1)
            if n > num:
                n -= num
                count += 1
            else:
                i, j = divmod(n, (count + 1))
                if not j:
                    return int(str(10 ** count + i - 1)[-1])
                else:
                    return int(str(10 ** count + i)[j - 1])
```

欢迎关注我的公众号: **清风Python**

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)


