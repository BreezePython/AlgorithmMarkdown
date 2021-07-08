# [剑指Offer34.二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/jian-zhi-offer34er-cha-shu-zhong-he-wei-zm7k8/)
> https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/jian-zhi-offer34er-cha-shu-zhong-he-wei-zm7k8/
> 
> 难度：中等

## 题目：

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

提示：

- 节点总数 <= 10000

## 示例：

```
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
```

## 分析

由于我们需要从头到尾遍历每一个二叉树的分支节点，所以采用深度优先的方法较合适。
在判断过程中，需要针对每个节点添加的val，在遍历后进行pop，才能保证仅添加当前分支的val值。


## 解题：

```python
class Solution:
    def pathSum(self, root, target):
        ret = []
        path = []

        def dfs(tree, num):
            if not tree:
                return
            num -= tree.val
            path.append(tree.val)
            if not (tree.left or tree.right) and num == 0:
                    ret.append(path[:])
            dfs(tree.left, num)
            dfs(tree.right, num)
            path.pop()
        dfs(root, target)
        return ret
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
