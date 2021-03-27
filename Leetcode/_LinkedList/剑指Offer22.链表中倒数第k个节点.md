# 剑指 Offer 22. 链表中倒数第k个节点
> https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
> 
> 难度：简单

## 题目：

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。


## 示例：

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

## 分析

这道题采用快慢指针的方式，定义一个计数器，fast指针先开始移动，当计数器走过K个数后，slow指针在开始移动。

当fast指针结束，slow指针指向的即是倒数第K个数

## 解题：

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        n = 0
        while fast:
            if n>=k:
                slow = slow.next
            fast = fast.next
            n += 1
        return slow
```

欢迎关注我的公众号: **清风Python**

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)
