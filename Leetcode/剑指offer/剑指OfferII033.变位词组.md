# [剑指OfferII033.变位词组](https://leetcode-cn.com/problems/sfvd7V/solution/shua-chuan-jian-zhi-offer-day15-ha-xi-bi-p57n/)
> https://leetcode-cn.com/problems/sfvd7V/solution/shua-chuan-jian-zhi-offer-day15-ha-xi-bi-p57n/
> 
> 难度：中等

## 题目
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。

注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。
 
提示：
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] 仅包含小写字母

## 示例

```
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
```

## 分析
这道题在难度方面并不高，思路其实剑指OfferII032类似的：
1. 我们创建一个哈希表s，key 为String，value 为List
2. 然后循环列表中的每个字符串，先将字符串排序
3. 再看排序后的字符串是否在哈希表中，如果在则追加，如果不在单独开辟一对key:value即可
4. 最终将哈希表的value值转化为列表返回即可。

但对于 **Python** 这里还有一个优化点的，如果按照上面的方式，我们需要创建一个哈希表嵌套列表的操作。
而且最终有需要将哈希表的value转化为列表再返回比较麻烦。
我们可以换个思路：
1. 我们单独创建一个哈希表s和列表li
2. 当哈希表中不存在排序后的字符串时，我们获取当前列表长度作为value(其实是列表的下标)
3. 然后向哈希表中插入 key = 排序后的字符串, value = 该字符串在列表中的下标。
4. 下次遇到同类型的字符串，我们直接在列表对应下标中插入该字符串即可。

## 解题
**Python:**
```python
class Solution:
    def groupAnagrams(self, strs):
        ret = []
        d = {}
        for i in strs:
            sort_i = ''.join(sorted(i))
            if sort_i in d:
                ret[d[sort_i]].append(i)
            else:
                d[sort_i] = len(ret)
                ret.append([i])
        return ret
```
**Java:**
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for (String str : strs) {
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String key = new String(array);
            ArrayList<String> list = map.getOrDefault(key, new ArrayList<String>());
            list.add(str);
            map.put(key, list);
        }
        return new ArrayList<List<String>>(map.values());
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)