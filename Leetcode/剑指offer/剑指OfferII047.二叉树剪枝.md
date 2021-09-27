# [剑指OfferII047.二叉树剪枝](https://leetcode-cn.com/problems/pOCWxh/solution/jian-zhi-offerii047er-cha-shu-jian-zhi-p-6u4g/)
> https://leetcode-cn.com/problems/pOCWxh/solution/jian-zhi-offerii047er-cha-shu-jian-zhi-p-6u4g/
> 
> 难度：中等

## 题目：
给定一个二叉树 根节点 root ，树的每个节点的值要么是 0，要么是 1。请剪除该二叉树中所有节点的值为 0 的子树。

节点 node 的子树为 node 本身，以及所有 node 的后代。

提示:
- 二叉树的节点个数的范围是 [1,200]
- 二叉树节点的值只会是 0 或 1


## 示例：

```
示例 1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1] 
解释: 只有红色节点满足条件“所有不包含 1 的子树”。下图为返回的答案。
    1               1
     \               \
      0       -->     0
     / \               \
    0   1               1
示例 2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]
解释: 
         1                 1
        / \                 \
       /   \                 \
      0     1      -->        1
     / \   / \                 \
    0   0 0   1                 1
示例 3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]
解释: 
         1                   1
        / \                 / \
       /   \               /   \
      1     1      -->    1     1
     / \   / \           / \     \
    1   1 0   1         1   1     1
   /
  0
```

## 分析
虽然这道题看似是让我们去剪枝，但其实仔细考虑下条件，我们从叶子节点网上逆推：
1. 左子树为空
2. 右子树为空
3. node.val == 0

当满足以上三个条件时，将该叶子节点删除(node = null)，即可。
通过深度优先搜索每个节点的子节点，递归返回，就是最终的答案了。
这里需要注意下root节点为空时，特殊判断。

## 解题：

```python []
class Solution:
    def pruneTree(self, root):
        if not root:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
```
```java []
class Solution {
    public TreeNode pruneTree(TreeNode root) {
        if( root == null) {
            return root;
        }
        root.left = pruneTree(root.left);
        root.right = pruneTree(root.right);
        if (root.val == 0 && root.left == null && root.right == null){
            root = null;
        }
        return root;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
