## [剑指OfferII010.和为k的子数组](https://leetcode-cn.com/problems/QTMn0o/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-jdnu/)
> https://leetcode-cn.com/problems/QTMn0o/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-jdnu/
> 
> 难度：中等

## 题目
给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。

提示:
- 1 <= nums.length <= 2 * 10 ^ 4
- -1000 <= nums[i] <= 1000
- -10 ^ 7 <= k <= 10 ^ 7

## 示例

```
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2
解释: 此题 [1,1] 与 [1,1] 为两种不同的情况

示例 2 :
输入:nums = [1,2,3], k = 3
输出: 2
```

## 分析
这道题目非常简洁，就是求数组中何为整数k的连续子数组个数。
如果这道题的取值没有负数，那就是标准的滑窗问题，但因为有了负数，滑窗思想不能用了。
通过分析，这道题应该属于我们上面列举四种情况的最后一种。具体思路如下：
1. 初始化一个空的哈希表和pre_sum=0的前缀和变量
2. 设置返回值ret = 0，用于记录满足题意的子数组数量
3. 循环数组的过程中，通过原地修改数组的方式，计算数组的累加和
4. 将当前累加和减去整数K的结果，在哈希表中查找是否存在
5. 如果存在该key值，证明以数组某一点为起点到当前位置满足题意，ret加等于将该key值对应的value
6. 判断当前的累加和是否在哈希表中，若存在value+1，若不存在value=1
7. 最终返回ret即可

但在这里要注意刚才说到的前缀和边界问题。
我们在计算这种场景时，需要考虑如果以数组nums[0]为开头的连续子数组就满足题意呢？
此时候我们的哈希表还是空的，没办法计算前缀和！所以遇到这类题目，都需要在哈希表中默认插入一个{0:1}的键值对，
用于解决从数组开头的连续子数组满足题意的特殊场景。
下面就开始解题吧！

## 解题
**Python:**
```python
class Solution:
    def subarraySum(self, nums, k):
        ret = pre_sum = 0
        pre_dict = {0: 1}
        for i in nums:
            pre_sum += i
            ret += pre_dict.get(pre_sum - k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
        return ret
```
**Java:**
```java 
class Solution {
    public int subarraySum(int[] nums, int k) {
        int pre_sum = 0;
        int ret = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int i : nums) {
            pre_sum += i;
            ret += map.getOrDefault(pre_sum - k, 0);
            map.put(pre_sum, map.getOrDefault(pre_sum, 0) + 1);
        }
        return ret;
    }
}
```


欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)