# 剑指Offer53-II.0～n-1中缺失的数字
> https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
> 
> 难度：简单

## 题目：

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。

在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

## 示例：

示例 1:

输入: [0,1,3]

输出: 2

示例 2:

输入: [0,1,2,3,4,5,6,7,9]

输出: 8

## 分析

分析

这道题其实就是一道数学题，如果考虑是中间缺失还是默认数字缺失，计算起来都很麻烦。
但如果只考虑列表长度就简单了，题目明确少了列表有且仅缺少一个数字，那么我们默认长度必为len(nums) + 1。

由于数字是从0开始的，则默认数字就是len(nums)，如此得到本应该的总和为:

`(0 + len(nums)) * (len(nums) + 1) // 2`，

将数字减去sum(nums)即为所得结果，就这么简单的道理。

## 解题：

```python
class Solution:
    def missingNumber(self, nums):
        length = len(nums) + 1
        return (length - 1) * length // 2 - sum(nums)
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
