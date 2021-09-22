# [剑指OfferII045.二叉树最底层最左边的值](https://leetcode-cn.com/problems/LwUNpT/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-do26g/)
> https://leetcode-cn.com/problems/LwUNpT/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-do26g/
> 
> 难度：中等

## 题目
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

提示:
- 二叉树的节点个数的范围是 [1,10 ^ 4]
- -2 ^ 31 <= Node.val <= 2 ^ 31 - 1 

## 示例：
```
示例 1:
输入:
    2
   / \
  1   3

输出:
1

示例 2:
输入:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
```

## 分析
首先，最简单的应该是BFS逐层遍历
1. 我们创建一个变量ret，用于记录每行的第一个val
2. 然后创建队列queue，由于题目说明至少有一个节点，则root无脑入队，开始while循环 
3. 判断每行的第一个节点，将ret变量更新为首个节点的值
4. 直到队列为空时，终止循环，返回ret即可。

## 解题

**Python:**

```python
class Solution:
    def findBottomLeftValue(self, root):
        queue = deque([root])
        ret = root.val
        while queue:
            for i in range(len(queue)):
                q = queue.popleft()
                if i == 0:
                    ret = q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return ret
```

**Java:**

```java
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int ret = root.val;
        while (!queue.isEmpty()) {
            int lg = queue.size();
            for (int i = 0; i < lg; i++) {
                TreeNode q = queue.poll();
                if (i == 0){
                    ret = q.val;
                }
                if (q.left != null) {
                    queue.add(q.left);
                }
                if (q.right != null) {
                    queue.add(q.right);
                }
            }
        }
        return ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)