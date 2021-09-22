# [剑指OfferII044.二叉树每层的最大值](https://leetcode-cn.com/problems/hPov7L/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-vo9a5/)
> https://leetcode-cn.com/problems/hPov7L/solution/shua-chuan-jian-zhi-offer-day21-dui-lie-vo9a5/
> 
> 难度：中等

## 题目：

给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

提示：
- 二叉树的节点个数的范围是 [0,10 ^ 4]
- -2 ^ 31 <= Node.val <= 2 ^ 31 - 1

## 示例：

```
示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \   \  
      5   3   9 
      
示例2：
输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \
        2   3
        
示例3：
输入: root = [1]
输出: [1]

示例4：
输入: root = [1,null,2]
输出: [1,2]
解释:      
           1 
            \
             2     
示例5：
输入: root = []
输出: []
```

## 分析
题目要求我们获取每一层的最大值，正好满足队列的出入队操作。
1. 首先我们需要初始化队列queue、及返回队列ret
2. 当队列不为空时，循环执行出入队
3. 访问每一层前，初始化num为最小值
4. 然后比较获取当前队列中的val最大值，并将最大值加入ret中
5. 根据每个出队的节点，判断该节点的左、右子树是否存在，若存在则执行入队操作
6. 循环3--5步骤，直到队列为空停止，并返回ret即可


## 解题：

**Python:**

```python
class Solution:
    def largestValues(self, root):
        ret, queue = [], deque()
        if root:
            queue.append(root)
        while queue:
            num = -float('inf')
            for i in range(len(queue)):
                q = queue.popleft()
                num = max(num, q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            ret.append(num)
        return ret
```

**Java:**

```java
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<Integer> ret = new LinkedList<>();
        if (root != null) {
            queue.add(root);
        }
        while (!queue.isEmpty()) {
            int num = Integer.MIN_VALUE;
            int lg = queue.size();
            for (int i = 0; i < lg; i++) {
                TreeNode q = queue.poll();
                num = Math.max(num, q.val);
                if (q.left != null) {
                    queue.add(q.left);
                }
                if (q.right != null) {
                    queue.add(q.right);
                }
            }
            ret.add(num);
        }
        return ret;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
