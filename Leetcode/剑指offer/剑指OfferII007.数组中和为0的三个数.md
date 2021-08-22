# [剑指OfferII007.数组中和为0的三个数](https://leetcode-cn.com/problems/1fGaJU/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-e2af/)
> https://leetcode-cn.com/problems/1fGaJU/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-e2af/
> 
> 难度：中等

## 题目
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？
请找出所有和为 0 且 不重复 的三元组。

提示：
- 0 <= nums.length <= 3000
- -10 ^ 5 <= nums[i] <= 10 ^ 5


## 示例

```
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
```

## 分析
这道题算是上一道题的升华版，那么三层for循环是不是可以走一波？按照这个数量级有点风险，但这种暴力解法就不展开了。
我们打算接着使用刚才双指针的思想，但是三个数该如何操作？无非是在双指针的外面套一层for循环而已。
这道题的数组是没有排序的，所以在前面单独介绍了Python和Java数组的排序操作。
另外需要注意的是，题目要求不重复的三元组，为了保持不重复，我们可以：
1. 使用集合进行去重
2. 指针偏移时，判断下一个val是否等于当前val，若等于则跳过的操作来实现
理解了这三点，有前一道题目解析的铺垫，就可以大胆操作了！
最后，还有一个优化点，如果第一个数字已经大于0了，那直接可以break了...
- # [剑指OfferII006.排序数组中两个数字之和](https://leetcode-cn.com/problems/kLl5u1/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-ygiw/)


## 解题

Python:

```python 
class Solution:
    def threeSum(self, nums):
        nums.sort()
        lg, ret = len(nums), []
        for i in range(lg - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = lg - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    val = nums[left]
                    while left < right and nums[left] == val:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return ret
```

Java: 

```java 
class Solution {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        int lg = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < lg; i++) {
            if (nums[i] > 0) break; 
            if (i > 0 && nums[i] == nums[i - 1]) continue; 
            int left = i + 1;
            int right = lg - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (total == 0) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++; 
                    left++;
                } else if (total < 0) left++;
                else if (total > 0) right--;
            }
        }
        return ans;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)