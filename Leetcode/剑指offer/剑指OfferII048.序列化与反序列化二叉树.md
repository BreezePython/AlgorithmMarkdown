## [剑指OfferII048.序列化与反序列化二叉树](https://leetcode-cn.com/problems/h54YBf/solution/jian-zhi-offerii048xu-lie-hua-yu-fan-xu-i5xul/)
> https://leetcode-cn.com/problems/h54YBf/solution/jian-zhi-offerii048xu-lie-hua-yu-fan-xu-i5xul/
> 
> 难度：中等

### 题目
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：
- 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
- 你并非必须采取这种方式，也可以采用其他的方法解决这个问题。
- 树中结点数在范围 [0, 10 ^ 4] 内
- -1000 <= Node.val <= 1000
### 示例
```
示例 1：
         1      
        / \     
       /   \    
      2     3   
           / \  
          4   5 

输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]
```

### 分析
大多数时候，我们所熟悉的树都是通过链式存储的非线性结构，但其实树还可以通过列表存储的线性结构来实现。
而这道题，在列表存储的基础上，让我们将列表转化为字符串，只是多了一道工序而已。
如果大家之前有了解过树的线性存储，相信这道题可以信手拈来。

#### BFS解题分析
- 这道题使用BFS的解题更为简单写，默认BFS时，需要判断当前节点是否有左、右子树
- 而此时，我们无需判断左右子树，当node为None时添加一个None到队列中即可。

#### DFS解题分析
- 在使用DFS时，势必将根节点放在第一个位置，可以方便我们反序列化，所以应该使用**前序遍历**。
- 遍历的时候同样注意，如果遇到空节点，需要将为空的节点也记录下来
- 即当一个子节点的左右节点都是None时，表示它其实是一个叶子节点。
- 反序列化时，同样通过前序遍历来实现，但注意默认的字符串转化为列表后，我们应该将从左到右遍历才满足条件
- Python我们可以反转列表或者使用deque的双端队列
- Java我们可以链表来实现

具体BFS、DFS解题如下：

### BFS解题

**Python:**

```python
from collections import deque

class Codec:
    
    def serialize(self, root):
        if not root:
            return ""
        dq = deque([root])
        res = []
        while dq:
            node = dq.popleft()
            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return []
        dataList = data.split(',')
        root = TreeNode(int(dataList[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                dq.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                dq.append(node.right)
            i += 1
        return root
```

**Java:**

```java
public class Codec {

    public String serialize(TreeNode root) {
        if(root == null){
            return "";
        }
        StringBuilder res = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            if(node != null){
                res.append("" + node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            }else{
                res.append("null");
            }
            res.append(",");
        }
        return res.toString();
    }

    public TreeNode deserialize(String data) {
        if(data == ""){
            return null;
        }
        String[] dataList = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(dataList[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            if(!"null".equals(dataList[i])){
                node.left = new TreeNode(Integer.parseInt(dataList[i]));
                queue.offer(node.left);
            }
            i++;
            if(!"null".equals(dataList[i])){
                node.right = new TreeNode(Integer.parseInt(dataList[i]));
                queue.offer(node.right);
            }
            i++;
        }
        return root;
    }
}
```

### DFS解题

**Python:**

```python
from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return 'None'
        root.left = self.serialize(root.left)
        root.right = self.serialize(root.right)
        return f"{root.val},{root.left},{root.right}"

    def deserialize(self, data):
        dq = deque(data.split(','))

        def dfs(li):
            val = li.popleft()
            if val == "None":
                return None
            root = TreeNode(int(val))
            root.left = dfs(li)
            root.right = dfs(li)
            return root
        return dfs(dq)
```

**Java:**

```java
public class Codec {

    public String serialize(TreeNode root) {
        if(root == null){
            return "null";
        }
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);  
    }

    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return dfs(queue);
    }

    private TreeNode dfs(Queue<String> queue) {
        String val = queue.poll();
        if("null".equals(val)){
            return null;
        }
        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = dfs(queue);
        root.right = dfs(queue);
        return root;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)