# 剑指Offer53-I.在排序数组中查找数字I
> https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
> 
> 难度：中等

## 题目：

统计一个数字在排序数组中出现的次数。

## 示例：

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

## 分析

遇到这种题，都不能说重拳出击了，简直是一套组合拳...

## 解题1：
内置collections.Counter函数快速解题

```python
from collections import Counter

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Counter(nums).get(target, 0)
```

## 解题2：
循环列表
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ret = 0
        for i in nums[nums.index(target):]:
            if i == target:
                ret += 1
        return ret
```

## 解题3：
二分查找
```python
class Solution:
    def search(self, nums: [int], target: int) -> int:
        def binary_search(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return binary_search(target) - binary_search(target - 1)
```

欢迎关注我的公众号: **清风Python**

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)
