# [剑指OfferII015.字符串中的所有变位词](https://leetcode-cn.com/problems/VabMRr/)
> https://leetcode-cn.com/problems/VabMRr/
> 
> 难度：中等

## 题目：
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

变位词 指字母相同，但排列不同的字符串。

提示:
- 1 <= s.length, p.length <= 3 * 10 ^ 4
- s 和 p 仅包含小写字母

## 示例：

```
示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。
```

## 分析
昨天的文章中，我们学习使用长度为26的数组，来建立字符串数量与数组下标对应关系的操作。
通过对应关系，判断数组相等的方式，来实现字母异位词的操作。如果忘记了可以复习下昨天的解题
- [剑指OfferII014.字符串中的变位词](https://leetcode-cn.com/problems/MPnaiL/solution/shua-chuan-jian-zhi-offer-day08-zi-fu-ch-pasw/)

那么今天的这道题，相比于14题有什么变化么？答案是几乎没有...
昨天我们在循环过程中判断如果找到异位词立即返回，今天的题目，我们只需要在遇到异位词时记录此时的起始index，保存在数组。
然后返回数组即可，就这么点差别，看我们ctrl c v 14题的解题，快速解题。

## 解题：

```python []
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr1, arr2, lg, ret = [0] * 26, [0] * 26, len(p), []
        if lg > len(s):
            return []
        for i in range(lg):
            arr1[ord(p[i]) - ord('a')] += 1
            arr2[ord(s[i]) - ord('a')] += 1
        if arr1 == arr2:
            ret.append(0)
        for i in range(lg,len(s)):
            arr2[ord(s[i]) - ord('a')] += 1
            arr2[ord(s[i - lg]) - ord('a')] -= 1
            if arr1 == arr2:
                ret.append(i - lg + 1)
        return ret
```

```java []
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] arr1 = new int[26];
        int[] arr2 = new int[26];
        List<Integer> list = new ArrayList<Integer>();
        if (p.length() > s.length()) {
            return list;
        }
        for (int i = 0; i < p.length(); i++) {
            arr1[p.charAt(i) - 'a']++;
            arr2[s.charAt(i) - 'a']++;
        }
        if (Arrays.equals(arr1, arr2)) {
            list.add(0);
        }
        for (int i = p.length(); i < s.length(); i++) {
            arr2[s.charAt(i - p.length()) - 'a']--;
            arr2[s.charAt(i) - 'a']++;
            if (Arrays.equals(arr1, arr2)) {
                list.add(i - p.length() + 1);
            }
        }
        return list;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
