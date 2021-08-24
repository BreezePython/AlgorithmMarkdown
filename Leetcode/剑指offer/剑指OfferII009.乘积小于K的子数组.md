# [剑指OfferII009.乘积小于K的子数组](https://leetcode-cn.com/problems/ZVAVXX/solution/jian-zhi-offerii009cheng-ji-xiao-yu-kde-q158e/)
> https://leetcode-cn.com/problems/ZVAVXX/solution/jian-zhi-offerii009cheng-ji-xiao-yu-kde-q158e/
> 
> 难度：中等

## 题目

给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。

提示: 
- 1 <= nums.length <= 3 * 104
- 1 <= nums[i] <= 1000
- 0 <= k <= 106

## 示例

```
示例 1:
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], 
[2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

示例 2:
输入: nums = [1,2,3], k = 0
输出: 0
```

## 分析
这道题乍一看满足滑窗的条件，让我们找**小于**K的**连续子数组**的个数，但这不是求最大最小滑窗的长度，而是要求子数组的个数。有点不满足公式啊？
别着急否定，让我们来画个图考虑下滑窗右边界移动这个操作与滑窗内子数组个数的关系吧！

通过画图我们发现，窗口每次移动后，ret都可以增加right - left + 1个子数组。这不就可以通过滑窗来解题了么？
但这里要注意一点：
如果数组中某个数字比K还大，则left会超过right，以保证有值，此时窗口长度为-1，无需计算。

注意：由于K<=10 ^ 6，nums[i]<=1000, 10 ^ 9 小于Integer.MAX_VALUE，所以Java使用int类型不会越界。

## 解题

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        left = ret = 0
        total = 1
        for right, num in enumerate(nums):
            total *= num
            while left <= right and total >= k:
                total //= nums[left]
                left += 1
            if left <= right:
                ret += right - left + 1
        return ret
```

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int left = 0;
        int ret = 0;
        int total = 1;
        for (int right = 0; right < nums.length; right++) {
            total *= nums[right];
            while (left <= right && total >= k) {
                total /= nums[left++];
            }
            if (left <= right) {
                ret += right - left + 1;
            }
        }
        return ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)