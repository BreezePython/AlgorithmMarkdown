# [剑指offerII019.最多删除一个字符得到回文](https://leetcode-cn.com/problems/RQku0D/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-b0ub/)
> https://leetcode-cn.com/problems/RQku0D/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-b0ub/
> 
> 难度：简单

## 题目
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

提示:
- 1 <= s.length <= 10 ^ 5
- s 由小写英文字母组成

## 示例

```
示例 1:
输入: s = "aba"
输出: true

示例 2:
输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符

示例 3:
输入: s = "abc"
输出: false
```

## 分析
这道题作为[剑指offerII018.有效的回文](https://leetcode-cn.com/problems/XltzEq/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-y5ua/)的进阶版，
我们需要在018的基础上注意，当出现不等于的时候，应该如何操作。由于我们不能判断到底左、右哪边不符合，所以必须都考虑一遍。思路如下：
1. 首先设置左、右指针分别指向字符串的首尾
2. 然后开始左右匹配，如果相等left+1，right -1
3. 如果不相等，记录当前left和right，然后构造一个方法check
4. 想check中分别传输[left + 1,right]和[left, right - 1]，若检查通过返回True否则返回False
5. 如果3中有一个为True，就表示为回文子串。

所以，我要这么写代码了么？不，我不想...
这样在代码上存在两次while的冗余，如何能让开始的时候也调用check方法呢？
我们让check始终返回left和right两个指针不就可以将两次while复用了。
这样怎么判断是否通过呢？如果最终left指针走过了字符串长度的一半以上，那肯定是满足要求的。
但这里要注意，在判断right - 1时，我们修改了字符串尾部的长度判断，所以这种条件时left只要等于字符串长度的一半就满足题意了。
这种判断完全是为了解决代码复用。最终Python和Java的思路如下:

## 解题

**Python:**
```python
class Solution:
    def validPalindrome(self, s):
        def check(l, r):
            while l <= r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            return l, r

        mid = len(s) // 2
        left, right = check(0, len(s) - 1)
        if left > mid:
            return True
        return check(left + 1, right)[0] > mid or check(left, right - 1)[0] == mid
```

**Java:**
```java
class Solution {
    public boolean validPalindrome(String s) {
        int[] idx = new int[2];
        int mid = s.length() / 2;
        idx = check(s, 0, s.length() - 1);
        if (idx[0] > mid) {
            return true;
        }
        return check(s, idx[0] + 1, idx[1])[0] > mid || check(s, idx[0], idx[1] - 1)[0] == mid;
    }

    private int[] check(String s, int l, int r) {
        while (l <= r) {
            if (s.charAt(l) != s.charAt(r)) {
                break;
            } else {
                l++;
                r--;
            }
        }
        return new int[]{l, r};
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)

