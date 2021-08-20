## [剑指Offer001.整数除法](https://leetcode-cn.com/problems/xoh6Oh/)
> https://leetcode-cn.com/problems/xoh6Oh/
>
> 难度：简单

## 题目：

给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

注意：

- 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2 ^ 31, 2 ^ 31−1]。本题中，如果除法结果溢出，则返回 2 ^ 31 − 1

提示:

- 2 ^ 31 <= a, b <= 2 ^ 31 - 1
- b != 0

## 示例：

```
示例 1：
输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7

示例 2：
输入：a = 7, b = -3
输出：-2
解释：7/-3 = truncate(-2.33333..) = -2

示例 3：
输入：a = 0, b = 1
输出：0

示例 4：
输入：a = 1, b = 1
输出：1
```

## 分析

首先这种不能使用xxx方法的题目，一般机试时是不会出的，因为限制不了编辑器，人工阅卷又需要耽误时间。
但正因为不会出现在机试中，所以在手撕算法时却会成为热门，所以请不要违背题意的直接使用乘、除提交题目。

拿示例一来说，一个最直观的方法就是循环使用a-b，计算减了多少次，即可得到结果。
但请注意a、b的取值范围，如果a为2 ^ 31−1，b为1那么仅一次就需要计算2 ^ 31−1次，所以这个思路是不可行的。
那么，既然不能从被除数上下手，能否通过除数进行操作呢？如果大家对二分搜索熟悉，相信很快能找到思路。

1. 初始化返回值ret = 0
2. 如果换成如果被除数大于除数，则除数扩大一倍
3. 若被除数仍大于除数，这除数再次扩大一倍
4. 直到除数下一次翻倍比被除数大时，将被除数减去除数，并将ret+=除数扩大的倍数，结束这一轮循环
5. 重复2、3、4，直到被除数小于除数，终止循环并返回ret即可。 

另外：在计算开始时，我们需要注意判断除数和被除数的正负号问题。如果是Python，只需要记录正负号即可。但对于Java而言，
由于负数的取值比正数大1，转换成正数计算会造成溢出，所以简单的方式是将数字转化为负数来进行比较。

## 解题：

```python
class Solution:
    def divide(self, a: int, b: int) -> int:
        ret = 0
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)

        def calc(x, y):
            n = 1
            while x > y << 1:
                y <<= 1
                n <<= 1
            return n, y

        while a >= b:
            cnt, val = calc(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        return ret - 1 if ret >= 2 ** 31 else ret
```

```java
class Solution {

    public int divide(int a, int b) {
        int flag = 0;
        if (a > 0) {
            a = -a;
            flag += 1;
        }

        if (b > 0) {
            b = -b;
            flag += 1;
        }
        int ret = calc(a, b);
        if (flag != 1 && ret == Integer.MIN_VALUE) {
            ret++;
        }
        return flag == 1 ? ret : -ret;
    }

    private int calc(int a, int b) {
        int ret = 0;
        while (a <= b) {
            int cnt = 1;
            int val = b;
            while (val >= Integer.MIN_VALUE >> 1  && a <= val << 1) {
                cnt += cnt;
                val += val;
            }
            ret -= cnt;
            a -= val;
        }
        return ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](