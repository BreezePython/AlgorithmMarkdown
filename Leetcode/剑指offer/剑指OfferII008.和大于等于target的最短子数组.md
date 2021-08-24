# [剑指OfferII008.和大于等于target的最短子数组](https://leetcode-cn.com/problems/2VG8Kg/)
> https://leetcode-cn.com/problems/2VG8Kg/
> 
> 难度：中等

## 题目

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度**最小**的 **连续子数组** [numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。

提示：
- 1 <= target <= 10 ^ 9
- 1 <= nums.length <= 10 ^ 5
- 1 <= nums[i] <= 10 ^ 5

进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

## 示例

```
示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

## 分析
根据题目，已经将刚才提到的关键字进行了加粗表示，首先看到连续子数组，我们就该考虑是否可以通过滑窗的思维去解题。
然后看到了长度最小的限制，分析题意滑窗思维没毛病。
那么刚才模板中说的题目条件是什么呢？满足滑窗内数字之和需要大于等于target。
返回值ret又是什么？符合条件的子数组长度。
模板中所有的架子都搭好了，往里面套代码吧！

## 解题

```python
class Solution:
    def minSubArrayLen(self, target, nums):
        left = total = 0
        ret = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                ret = min(ret, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if ret > len(nums) else ret
```

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int total = 0;
        int ret = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++) {
            total += nums[right];
            while (total >= target) {
                ret = Math.min(ret, right - left + 1);
                total -= nums[left++];
            }
        }
        return ret > nums.length ? 0 : ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)