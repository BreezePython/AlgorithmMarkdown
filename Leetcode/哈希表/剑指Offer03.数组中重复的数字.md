# [剑指Offer03.数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)
> https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
> 
> 难度：简单

## 题目

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

限制：
- 2 <= n <= 100000

## 示例

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

## 分析

显然最快的方式是通过集合/哈希表判断是否存在。偷懒的可以Counter后计算，但这样内存消耗过大。
最好的是循环数组，判断该数字是否在哈希表中，如果存在返回，不存在添加。

## 遍历数组
```python
class Solution:
    def findRepeatNumber(self, nums):
        comp = set()
        for i in nums:
            if i in comp:
                return i
            comp.add(i)
```

## Counter解题

```python
from collections import Counter
class Solution:
    def findRepeatNumber(self, nums):
        return sorted(Counter(nums).items(),key = lambda x: -x[1])[0][0]
```


欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)