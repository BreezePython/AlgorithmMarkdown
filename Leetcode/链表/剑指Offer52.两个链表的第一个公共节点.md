# [剑指Offer52.两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/jian-zhi-offer52liang-ge-lian-biao-de-di-yj5l/)
> https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/jian-zhi-offer52liang-ge-lian-biao-de-di-yj5l/
> 
> 难度：中等

## 题目
![image.png](https://pic.leetcode-cn.com/1626798750-TWmAMY-image.png)

注意：
- 如果两个链表没有交点，返回 null.
- 在返回结果后，两个链表仍须保持原有的结构。
- 可假定整个链表结构中没有循环。
- 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
- 本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


## 分析
这道题比较容易想到的是，创建一个hash表，然后循环依次A，将A的所有节点添加至Hash表中。
再循环依次B，每次判断B的当前节点是否在hash表中。
代码如下：
```python
class Solution:
    def getIntersectionNode(self, headA, headB):
        d = {}
        while headA:
            d[headA] = headA
            headA = headA.next
        while headB:
            if d.get(headB):
                return headB
            headB = headB.next
        return None
```
![image.png](https://pic.leetcode-cn.com/1626798816-gkZqaJ-image.png)


这样的思路可以通过，但是题目说了**程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。**

hash表构造了额外的O(n)空间复杂度，那么如何来实现使用O(1)的时间复杂度完成呢？来看看下面的图：

![demo1.gif](https://pic.leetcode-cn.com/1626799286-OwUPSC-demo1.gif)


如果两个链表相交，那么：
`X + 1 + Z + Y 必然等于 Y + 1 + Z + X`

所以我们可以使用上图的方式，通过双指针的解法，来完成这道题目。具体代码如下：

![image.png](https://pic.leetcode-cn.com/1626798689-xAOWDQ-image.png)

```python
class Solution:
    def getIntersectionNode(self, headA, headB):
        x, y = headA, headB
        while x != y:
            x = x.next if x else headB
            y = y.next if y else headA
        return x
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)