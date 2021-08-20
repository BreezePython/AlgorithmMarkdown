# [剑指OfferII002.二进制加法](https://leetcode-cn.com/problems/JFETK5/solution/shua-chuan-jian-zhi-offer-day02-zheng-sh-obx6/)
> https://leetcode-cn.com/problems/JFETK5/solution/shua-chuan-jian-zhi-offer-day02-zheng-sh-obx6/
> 
> 难度：简单

## 题目

给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字 1 和 0。

提示：
- 每个字符串仅由字符 '0' 或 '1' 组成。
- 1 <= a.length, b.length <= 10^4
- 字符串如果不是 "0" ，就都不含前导零。

## 示例

```
示例 1:
输入: a = "11", b = "10"
输出: "101"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
```

## 分析
正如昨天提到的，在做整数题目时，Python与Java的差别是什么呢？
- Python： 放心大胆无脑冲！
- Java：在越界的边缘战战兢兢。

所以很多时候Python在刷题上简直是作弊，拿这道题来说，a、b的长度都为10 ^ 4，
在Java中是没办法表示的，对于Python只需要一行，简直了：
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```
可如果在面试中这样写，那真是一首凉凉送给你。 但这毕竟是一道简单题目，作为今天的开胃菜，并没有太大的难度。

对于这道题，我们只需要牢记以下**三点**即可：
1. 逢二进一是二进制的法则
2. 进位的这个一，我们需要找个变量才存储它，才能在下一次的循环中获取
3. 对于不等长的字符串，我们需要进行适当的优化与判断

## 解题

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder ret = new StringBuilder();
        int count = 0;
        for (int i = a.length() - 1, j = b.length() - 1;
             i >= 0 || j >= 0 || count > 0; i--, j--) {
            int total = count;
            total += i >= 0 ? a.charAt(i) - '0' : 0;
            total += j >= 0 ? b.charAt(j) - '0' : 0;
            count = total > 1 ? 1 : 0;
            ret.append(total - count * 2);
        }
        return ret.reverse().toString();
    }
}
```

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret, count = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or count:
            if i >= 0:
                count += ord(a[i]) - ord('0')
            if j >= 0:
                count += ord(b[j]) - ord('0')
            ret += str(count % 2)
            count //= 2
            i, j = i - 1, j - 1
        return ret[::-1]
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)