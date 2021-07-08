# [LCP28.采购方案](https://leetcode-cn.com/problems/4xy4Wx/solution/)
> https://leetcode-cn.com/problems/4xy4Wx/solution/
> 难度：简单

## 题目：

小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

提示：

2 <= nums.length <= 10^5

1 <= nums[i], target <= 10^5

## 示例：

示例 1：

输入：nums = [2,5,3,5], target = 6

输出：1

解释：预算内仅能购买 nums[0] 与 nums[2]。

示例 2：

输入：nums = [2,2,1,9], target = 10

输出：4

解释：符合预算的采购方案如下：

nums[0] + nums[1] = 4

nums[0] + nums[2] = 3

nums[1] + nums[2] = 3

nums[2] + nums[3] = 10

## 分析

## 解题1：

```python
import bisect


class Solution:
    def purchasePlans(self, nums, target):
        def get_num(n):
            if n < 0:
                return 0
            return (1 + n) * n // 2

        total = 0
        nums.sort()
        nums = nums[:bisect.bisect_left(nums, target - nums[0] + 1)]
        mid = bisect.bisect_right(nums, target // 2)
        total += get_num(mid - 1)
        length = len(nums)
        while mid < length:
            num = bisect.bisect_left(nums, target - nums[mid] + 1)
            if num <= mid:
                total += num
            mid += 1
        return total % (10 ** 9 + 7)
```

## 解题2：

```python
import bisect


class Solution:
    def purchasePlans(self, nums, target):
        nums.sort()
        total = 0
        for i, n in enumerate(nums):
            p = bisect.bisect(nums, target - n, 0, i)
            total += p
        return total % 1000000007
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
