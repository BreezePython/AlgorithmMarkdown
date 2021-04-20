# 
> https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/comments/
> 
> 难度：中等

## 题目：

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

## 示例：

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

输入：s = "aab"
输出：["aab","aba","baa"]

```

## 分析

标准的回溯解题，与[47.全排列2](https://leetcode-cn.com/problems/permutations-ii/)基本同源

## 解题：

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        ret = []
        path = []
        s =sorted(list(s))
        stage = [0 for _ in s]
        def dfs(li):
            if len(li) == len(path):
                ret.append(''.join(path[:]))
            for i in range(len(li)):
                if stage[i] == 1:
                    continue
                if i > 0 and li[i] == li[i -1] and stage[i -1] == 0:
                    continue
                path.append(li[i])
                stage[i] = 1
                dfs(li)
                path.pop()
                stage[i] = 0
        dfs(s)
        return ret
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
