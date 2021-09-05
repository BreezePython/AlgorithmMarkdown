## [剑指offerII021.删除链表的倒数第n个结点](https://leetcode-cn.com/problems/SLwz0R/solution/shua-chuan-jian-zhi-offer-day11-lian-bia-tuyw/)
> https://leetcode-cn.com/problems/SLwz0R/solution/shua-chuan-jian-zhi-offer-day11-lian-bia-tuyw/
> 
> 难度：中等

## 题目：

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

提示：

- 链表中结点的数目为 sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## 示例：

```
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
```

## 分析
遇到这种题多了其实就是公式，数组中有快慢指针，链表同样也可以创建快慢两个指针。
初始右指针先跑N，然后左指针在和右指针开始同步向前。
当右指针到达末尾时：
`left.next = left.next.next`即可!
这里需要注意，N的取值小于等于链表的长度。
这里就需要排除下当右指针跑了N后，已经超出链表，那么代表链表长度与N相等。
那倒数第N个数就是链表头，此时只需要返回head.next即可。
仔细分析，就是如此简单...

## 解题：
**Python:**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        left = right = head
        count = 0 
        while count < n:
            right = right.next
            count += 1
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
```
**Java:**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode left = head;
        ListNode right = head;
        int count = 0;
        for (int i = 0; i < n; i++) {
            right = right.next;
        }
        if (right == null) {
            return head.next;
        }
        while (right.next != null) {
            left = left.next;
            right = right.next;
        }
        left.next = left.next.next;
        return head;
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
