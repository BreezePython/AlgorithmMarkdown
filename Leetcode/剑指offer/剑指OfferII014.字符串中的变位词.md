# [剑指OfferII014.字符串中的变位词](https://leetcode-cn.com/problems/MPnaiL/solution/shua-chuan-jian-zhi-offer-day08-zi-fu-ch-pasw/)
> https://leetcode-cn.com/problems/MPnaiL/solution/shua-chuan-jian-zhi-offer-day08-zi-fu-ch-pasw/
> 
> 难度：中等

## 题目
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

提示：
- 1 <= s1.length, s2.length <= 10^4
- s1 和 s2 仅包含小写字母

## 示例

```
示例 1：
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例 2：
输入: s1= "ab" s2 = "eidboaoo"
输出: False
```

## 分析
正如上面说到的，双指针的解题思维不仅适用于数组，在字符串中也是适用的。
这道题相信在做过了前面第八、第九题后，可以一眼看出是一道双指针题目。
只不过从int[]的数组转化为了字符串而已。既然数组的双指针我们会做，那么**我们只需要将字符串转换为数组即可。**
由于本题仅包含小写字母，所以我们维护一个长度为26的数组，使用数组index对应的value值对应a-z字符出现的次数。
那么，为了便于理解我们维护两个数组，arr1、arr2分别表示s1、s2的转换。
然后通过循环逐次判断arr1是否等于arr2，等相等时，表示结果成立return True
如果整体循环结束后，仍未出现相等的场景，则判断结果为False，具体代码如下。

## 解题
**Python:**
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2, lg = [0] * 26, [0] * 26, len(s1)
        if lg > len(s2):
            return False

        for i in range(lg):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        for j in range(lg, len(s2)):
            if arr1 == arr2:
                return True
            arr2[ord(s2[j - lg]) - ord('a')] -= 1
            arr2[ord(s2[j]) - ord('a')] += 1
        return arr1 == arr2
```

**Java:**
```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] arr1 = new int[26];
        int[] arr2 = new int[26];
        if (s1.length() > s2.length()){
            return false;
        }
        for (int i = 0; i < s1.length(); i++) {
            arr1[s1.charAt(i) - 'a']++;
            arr2[s2.charAt(i) - 'a']++;
        }
        for (int i = s1.length(); i < s2.length(); i++) {
            if (Arrays.equals(arr1, arr2)) {
                return true;
            }
            arr2[s2.charAt(i - s1.length()) - 'a']--;
            arr2[s2.charAt(i) - 'a']++;
        }
        return Arrays.equals(arr1, arr2);
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)