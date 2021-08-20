# [剑指OfferII004.只出现一次的数字](https://leetcode-cn.com/problems/WGki4K/solution/shua-chuan-jian-zhi-offer-day02-zheng-sh-tlce/)
> https://leetcode-cn.com/problems/WGki4K/solution/shua-chuan-jian-zhi-offer-day02-zheng-sh-tlce/
> 
> 难度：中等

## 题目

给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。
请你找出并返回那个只出现了一次的元素。

提示：
- 1 <= nums.length <= 3 * 10 ^ 4
- -2 ^ 31 <= nums[i] <= 2 ^ 31 - 1
- nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

## 示例

```
示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,100]
输出：100
```

## 分析
如果考虑进阶中说到的不使用额外空间，那这道题真的是一道很简单的题目了。我们可以通过以下两种方法实现：
- 哈希表
  1. 创建一个哈希表
  2. 循环数组，将每个元素挨个加入哈希表中
  3. 遍历哈希表中的数据，查找哪个数字只出现了一次返回。

- 集合+数学
  1. 既然数组中只有一个数出现1次，其他的都出现三次，那么我们先创建一个集合
  2. 将数组加入集合s中，保持每个数字的唯一性
  3. 然后分别求sum(nums)、sum(s)
  4. 将sum(s) * 3 - sum(nums)会得到什么结果，是否为多那个只出现一次数字所缺失的两倍数字
  5. 然后将上一步的结果除以2，就得到了最终的结果。

以上两种方式，均可以计算出结果，但是都因为开辟了额外空间而不满足进阶的要求。那么，进阶该如何操作呢？
这里先简单介绍下力扣136题，只出现一次的数字。
> 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

遇到这道题同样上面的两个方法可以使用，但通过昨天的学习，我们应该第一时间想到异或操作，相同的二进制异或为0。
那么将数组挨个异或后的结果，不就是那个数字了么？

理解了这个思路，再看当前这道题目。这里我们有三个相同的数字，没办法通过异或操作完成判断，那如何换一种思路实现呢？
让我们看看下面这张图吧：

如果我们可以将所有的数字都转化为二进制，然后根据每一位对3其余，最终不就是我们要的结果吗？
最方便的是我们创建一个32位长度的数组，然后针对每个数字的二进制位对该数组对应下标进行累加，最终计算结果。
这里存在一个空间复杂度的计算规则，跟时间复杂度类似，**如果是常数的空间申请，是可以忽略为O(1)的。**
但为了严格按照题目要求，我们通过左位移配合二进制加法来实现累加操作，具体如图：

1. 初始ret = 0
2. 循环32位二进制位数i
3. 计算循环数组该i位之和对3求余
4. 若余数为1，则 ret |= 1 << i即可
5. 最终返回ret即可

这里要注意下由于Python是无符号位的二进制，所以需要对最高位进行判断。
若为1则表示负数，需要对ret进行减等操作。

## 解题

```python
class Solution:
    def singleNumber(self, nums) -> int:
        ret = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += num >> i & 1
            if cnt % 3:
                if i == 31:
                    ret -= (1 << i)
                else:
                    ret |= 1 << i
        return ret
```

```java
class Solution {
    public int singleNumber(int[] nums) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            int cnt = 0;
            for (int num : nums) {
                cnt += num >> i & 1;
            }
            if (cnt % 3 != 0) {
                ret |= 1 << i;
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