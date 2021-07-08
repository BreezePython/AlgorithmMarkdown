# 剑指 Offer 24. 反转链表
> https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
> 
> 难度：简单

## 题目：

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

限制：

0 <= 节点个数 <= 5000

## 示例：

示例:

输入: 1->2->3->4->5->NULL

输出: 5->4->3->2->1->NULL

## 分析

本题是一道基本的链表滚动赋值，通过设置pre和cur和临时tmp三个指针，进行指针交替滚动，完成翻转

## 解题：

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,pre = head,None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```

欢迎关注我的公众号: **清风Python**

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)
