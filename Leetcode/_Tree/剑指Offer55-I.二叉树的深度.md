# 剑指Offer55-I.二叉树的深度
> https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
> 
> 难度：简单

## 题目：

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，
最长路径的长度为树的深度。

提示：

节点总数 <= 10000
注意：本题与主站 104题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

## 示例：

例如：

给定二叉树 [3,9,20,null,null,15,7]，
```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度3 。


## 分析

遇到树的问题，可以无脑优先考虑递归的方式。本地就是树的最基础入门题...

## 解题：

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
