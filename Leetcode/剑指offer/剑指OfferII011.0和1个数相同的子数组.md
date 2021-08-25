# [剑指OfferII011.0和1个数相同的子数组](https://leetcode-cn.com/problems/A1NYOS/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-4q9c/)
> https://leetcode-cn.com/problems/A1NYOS/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-4q9c/
> 
> 难度：中等

## 题目

给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

提示：
- 1 <= nums.length <= 105
- nums[i] 不是 0 就是 1

## 示例

```
示例 1:
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。

示例 2:
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
```

## 分析
如果光看示例容易让我们误以为奇数下标为0，偶数下标为1，或者每两个下标长度判断一次结果等偏激的思想。
但当我们遇到连续0 或者连续1等特殊场景时，明显就不适用了。那么该如何变换后，可以适配前缀和的解题思维呢？
我们不妨将所有0转化为-1，那么如果遇到了相同数量的0和1，累加之后的结果就为0,不是就又转化为前缀和的思想了么？
解题思路如下：
1. 初始化哈希表，并添加{0:-1}
2. 声明前缀和变量pre_sum = 0，最大子数组长度返回值ret = 0
3. 循环数组，若元素为0，pre_sum - 1,反之pre_sum + 1
4. 判断哈希表中是否存在值为pre_sum的key
5. 若存在pre_sum的key,更新ret为max(ret, 当前下标 - key对应的value + 1)
6. 最终返回ret即可

## 解题
**Python:**
```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_dict = {0: -1}
        ret = pre_sum = 0
        for index, num in enumerate(nums):
            pre_sum += -1 if num == 0 else 1
            if pre_sum in pre_dict:
                ret = max(ret, index - pre_dict[pre_sum])
            else:
                pre_dict[pre_sum] = index
        return ret
```
**Java**
```java
class Solution {
    public int findMaxLength(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int pre_sum = 0;
        int ret = 0;
        for (int i = 0; i < nums.length; i++) {
            pre_sum += nums[i] == 0 ? -1 : 1;
            if (map.containsKey(pre_sum)) {
                ret = Math.max(ret, i - map.get(pre_sum));
            } else {
                map.put(pre_sum, i);
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