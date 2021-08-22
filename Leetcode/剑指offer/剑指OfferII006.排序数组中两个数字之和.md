# [剑指OfferII006.排序数组中两个数字之和](https://leetcode-cn.com/problems/kLl5u1/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-ygiw/)
> https://leetcode-cn.com/problems/kLl5u1/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-ygiw/
> 
> 难度：简单

## 题目

给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，
所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。

假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

提示：
- 2 <= numbers.length <= 3 * 10 ^ 4
- -1000 <= numbers[i] <= 1000
- numbers 按 递增顺序 排列
- -1000 <= target <= 1000
- 仅存在一个有效答案


## 示例
```
示例 1：
输入：numbers = [1,2,4,6,10], target = 8
输出：[1,3]

解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
示例 2：
输入：numbers = [2,3,4], target = 6
输出：[0,2]

示例 3：
输入：numbers = [-1,0], target = -1
输出：[0,1]
```

## 分析
这可能是力扣有史以来最简单的一道题了，为什么？因为力扣第一题两数之和就跟这道题神似。
但是注意，两数之和是无序的，而这道题是有序的，所以是不是更简单呢？

当然两数之和可以使用的暴力双层循环和Hash表，这道题也一样可以。
但双层for循环是O(n ^ 2)的复杂度，而Hash表虽然时间复杂度是O(n)，但空间复杂度一样是O(n).

然而，对于有序数组的两数之和，我们可以使用刚才提到的首尾双指针的解题思路来完成该题目。
1. 首先设置left、right指针分别指向数组的首、尾
2. 判断number[left] + number[right] 的和total与target的大小
3. 如果total > target,right 右移
4. 如果total < target,left 左移
5. 由于结果必然存在，最终返回left和right即可

时间复杂度O(n),空间复杂度O(1)
## 解题
Python:
```python
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```
Java:
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (left < right) {
            int total = numbers[left] + numbers[right];
            if (total == target) {
                return new int[]{left, right};
            } else if (total > target) {
                right--;
            } else {
                left++;
            }
        }
        return new int[2];
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)