# [剑指OfferII046.二叉树的右侧视图](https://leetcode-cn.com/problems/WNC0Lk/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-n360i/)
> https://leetcode-cn.com/problems/WNC0Lk/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-n360i/
> 
> 难度：中等

## 题目
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

提示:
- 二叉树的节点个数的范围是 [0,100]
- -100 <= Node.val <= 100 

## 示例

```
示例 1:
        1
       / \
      2   3
       \   \
        5   4

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:
输入: [1,null,3]
输出: [1,3]

示例 3:
输入: []
输出: []
```

## 分析
这道题，使用简单的BFS逐层遍历即可解题
1. 我们创建一个列表ret，用于记录每行的最右节点的val
2. 然后创建队列queue，当root不为空时，将root加入队列，然后开始while循环 
3. 判断每行的最后一个节点，并将该节点的值加入ret列表中
4. 根据每个出队的节点，判断该节点的左、右子树是否存在，若存在则执行入队操作
6. 直到队列为空时，终止循环，返回ret即可


## 解题

**Python:**

```python
class Solution:
    def rightSideView(self, root):
        queue, ret = deque(), []
        if root:
            queue.append(root)
        while queue:
            lg = len(queue)
            for i in range(lg):
                q = queue.popleft()
                if i == lg - 1:
                    ret.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return ret
```

**Java:**

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        if (root != null) {
            queue.add(root);
        }
        List<Integer> ret = new LinkedList<>();
        while (!queue.isEmpty()) {
            int lg = queue.size();
            for (int i = 0; i < lg; i++) {
                TreeNode q = queue.poll();
                if (i == lg - 1) {
                    ret.add(q.val);
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