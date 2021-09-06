# [剑指offerII024.反转链表](https://leetcode-cn.com/problems/UHnkqh/solution/shua-chuan-jian-zhi-offer-day12-lian-bia-190d/)
> https://leetcode-cn.com/problems/UHnkqh/solution/shua-chuan-jian-zhi-offer-day12-lian-bia-190d/
> 
> 难度：简单

## 题目：
给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。

提示：
- 链表中节点的数目范围是 [0, 5000]
- -5000 <= Node.val <= 5000

## 示例：

![image.png](https://pic.leetcode-cn.com/1630926655-feRiyg-image.png)

## 分析
链表不同于数组，可以通过获取数组的长度然后递减完成逆序。
日常的算法题目中链表多是单向的，我们想获取到最后一个节点就必须要挨个的遍历直到获取到链表末尾。
所以,链表逆序(反转)的题目就出现的理所当然了。
这道题是一个简单的链表逆序，主要就是考察链表的截断与重定向问题。
具体来说就是创建一个空节点，然后从链表头逐个反转。
千言万语不及画几张图，我们循环2-3的操作，即可完成链表反转...

![](https://pic.leetcode-cn.com/1630926680-ONbsff-2021-09-06_16-57-18.png)
![](https://pic.leetcode-cn.com/1630926684-bhIYWI-2021-09-06_16-58-29.png)
![](https://pic.leetcode-cn.com/1630931573-XpQJHk-2021-09-06_20-31-19.png)



## 解题：
```python []
class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre
```

```java []
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null){
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
