# [剑指OfferII032.有效的变位词](https://leetcode-cn.com/problems/dKk3P7/solution/shua-chuan-jian-zhi-offer-day15-ha-xi-bi-5pqx/)
> https://leetcode-cn.com/problems/dKk3P7/solution/shua-chuan-jian-zhi-offer-day15-ha-xi-bi-5pqx/
> 
> 难度：简单

## 题目
给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。

注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

提示:
- 1 <= s.length, t.length <= 5 * 10 ^ 4
- s and t 仅包含小写字母


## 示例

```
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

示例 3:
输入: s = "a", t = "a"
输出: false
```

## 分析
在不看进阶的情况下，这道题其实用不到哈希表，因为s和t只包含小写字母，我们在字符串和数组那章节已经讲过了这种题目的快速解法。
我们通过构造一个长度为26的数组对应26个英文字母(嗯...突然想起，谭警官的28个英文字母倒背如流，怕了怕了...)
通过字符串与ascii对应的方式完成匹配，这套路用的太多就不细讲了。
但是，进阶中说了，如果字符串包含unicode字符串怎么办？
怎么办，凉拌....直接上哈希表就行了啊！其他操作和数据没什么区别，只是换成了哈希表的对应方法而已么。

## 数组解题
**Python:**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        comp = [0] * 26
        for i in s:
            comp[ord(i) - 97] += 1
        for j in t:
            index = ord(j) - 97
            if comp[index] < 1:
                return False
            comp[index] -= 1
        return True
```
**Python:**
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length() || s.equals(t)) {
            return false;
        }
        int[] arr = new int[26];
        for (char i:s.toCharArray()) {
            arr[i - 97]++;
        }
        for (char j:t.toCharArray()) {
            arr[j - 97]--;
            if (arr[j - 97] < 0){
                return false;
            }
        }
        return true;
    }
}
```

## 哈希表解题
**Python:**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s != t and Counter(s) == Counter(t)
```
**Python:**
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length() || s.equals(t)) {
            return false;
        }
        HashMap<Character, Integer> arr = new HashMap<>();
        for (char i : s.toCharArray()) {
            arr.put(i, arr.getOrDefault(i, 0) + 1);
        }
        for (char j : t.toCharArray()) {
            if (!arr.containsKey(j) || arr.get(j) == 0)
                return false;
            arr.put(j, arr.get(j) - 1);
        }
        return true;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)