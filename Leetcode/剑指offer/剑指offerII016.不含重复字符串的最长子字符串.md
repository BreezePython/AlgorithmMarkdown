# [剑指offerII016.不含重复字符串的最长子字符串](https://leetcode-cn.com/problems/wtcaE1/solution/shua-chuan-jian-zhi-offer-day09-zi-fu-ch-tb4t/)
> https://leetcode-cn.com/problems/wtcaE1/solution/shua-chuan-jian-zhi-offer-day09-zi-fu-ch-tb4t/
> 
> 难度：中等

## 题目：

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

提示：
- 0 <= s.length <= 5 * 10 ^ 4
- s 由英文字母、数字、符号和空格组成

## 示例：

```
示例1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
```

## 分析：
这道题同样是通过滑动窗口来解题，只不过这次的边界获取要通过哈希表来实现。
1. 首先我们创建一个哈希表calc，并且初始化左边界left = 0，默认返回值ret = 0
2. 下来我们从0开始遍历字符串
3. 每当遍历到字符串中的一个字符时，首先需要判断该字符是否在哈希表calc中
4. 如果该字符串没有在哈希表中，表示该字符不重复，无需移动左边界，将该字符串及对应下标加入哈希表中
5. 如果该字符存在哈希表中，表示找到了重复的元素，此时我们需要移动左边界left
    - 若left小于哈希表中该字符对应的index下标，则移动至index + 1（因为index已经重复了，需要跳过）
    - 若left大于哈希表中该字符对应的index下标，表示重复的内容在左边界以外，忽略即可
    - 将当前字符串对应的下标更新哈希表中该字符串对应的下标
6. 每次更新左边界后，比较当前滑窗长度与返回值大小并更新返回值
7. 最终返回ret即可。

## 解题：
**Python:**
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        calc = {}
        left = 0
        ret = 0
        for i, j in enumerate(s):
            if j in calc:
                # 如果重复的数字出现在l之前忽略，否则了跳到该值的下一个位置
                left = max(left, calc[j] + 1)
            calc[j] = i
            ret = max(ret, i - left + 1)
        return ret
```
**Java:**
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> calc = new HashMap<>();
        int left = 0;
        int ret = 0;
        for (int i = 0; i < s.length(); i++) {
            if (calc.get(s.charAt(i)) != null) {
                left = Math.max(left, calc.get(s.charAt(i)) + 1);
            }
            calc.put(s.charAt(i), i);
            ret = Math.max(ret, i - left + 1);
        }
        return ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
