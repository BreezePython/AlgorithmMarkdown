# [剑指offerII018.有效的回文](https://leetcode-cn.com/problems/XltzEq/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-y5ua/)
> https://leetcode-cn.com/problems/XltzEq/solution/shua-chuan-jian-zhi-offer-day10-zi-fu-ch-y5ua/
> 
> 难度：简单

## 题目：
给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，将空字符串定义为有效的 回文串 。

提示：
- 1 <= s.length <= 2 * 10 ^ 5 
- 字符串 s 由 ASCII 字符组成 

## 示例：

```
示例 1:
输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: s = "race a car"
输出: false
解释："raceacar" 不是回文串
```

## 分析
### 无脑判断思维
对于回文子串，最为简单的思维就是，将子串过滤并保存成合规字符串，然后正序逆序遍历如果都相等代表是回文子串。
但这样有一个计算的时间浪费，如果这个字符串长度为2 * 10 ^ 5，我们的算法需要将这么大的数组拆分反转。
然后在一个一个比较，但此时也许字符串的首尾第一个字符就是不一样的，完全没必要浪费这么大周折啊！
所以我们应该考虑是否有更为便捷的思路。

### 解题：
```python []
class Solution:
    def isPalindrome(self, s):
        strs = ""
        for i in s:
            if i.isalnum():
                strs += i.lower()
        return strs == strs[::-1]
```
```java []
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                str.append(Character.toLowerCase(c));
            }
        }
        return str.toString().equals(new StringBuffer(str).reverse().toString());
    }
}
```

### 双指针思维
上面说到便捷高效的思路，该是什么呢？没错，就是用到烂的双指针。
1. 我们设置头尾双指针，然后分别向中间逼近
2. 当left或right指向的内容不在考虑范围内时跳过
3. 当left与right所指的字符不相等时立即终止
4. 如果循环结束仍未终止则返回True即可

### 解题：
```python []
class Solution:
    def isPalindrome(self, s):
        left, right, flag = 0, len(s) - 1, False
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and right > left:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
```

```java []
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left += 1;
            } else if (!Character.isLetterOrDigit(s.charAt(right))) {
                right -= 1;
            } else {
                char char1 = Character.toLowerCase(s.charAt(left++));
                char char2 = Character.toLowerCase(s.charAt(right--));
                if (char1 != char2) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)