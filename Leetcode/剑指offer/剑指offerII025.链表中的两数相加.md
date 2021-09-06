# [剑指offerII025.链表中的两数相加](https://leetcode-cn.com/problems/lMSNwu/solution/shua-chuan-jian-zhi-offer-day13-lian-bia-cl27/)
> https://leetcode-cn.com/problems/lMSNwu/solution/shua-chuan-jian-zhi-offer-day13-lian-bia-cl27/
>
> 难度：中等

## 题目：

给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

可以假设除了数字 0 之外，这两个数字都不会以零开头。

提示：

- 链表的长度范围为 [1, 100]
- 0 <= node.val <= 9
- 输入数据保证链表代表的数字无前导 0

## 示例：

![](https://pic.leetcode-cn.com/1630931028-KQcpyj-image.png)

```
示例1：
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]


示例2：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]


示例3：
输入：l1 = [0], l2 = [0]
输出：[0]
```

## 分析

- [2.两数相加](https://leetcode-cn.com/problems/add-two-numbers/solution/2-liang-shu-xiang-jia-biao-zhun-de-lian-c85p9/)

这道题目是力扣的第二题两数相加的进阶版本。第二题是整数从低位向高位保存求加和。 但是这道题却是整数从高位到低位求加和的操作。由于是单向链表，当低位存在进位时，我们没办法返回到之前的节点进行进位操作。
所以这道题，我们需要先反转链表后，在进行加法操作，最后在将加和的结果反转后输出。 由于上一道题目：

- [剑指offerII024.反转链表](https://leetcode-cn.com/problems/UHnkqh/solution/shua-chuan-jian-zhi-offer-day12-lian-bia-190d/)

我们已经写好了反转链表的方法，所以在这里就可以直接复用了！具体解法如下：

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

    def addTwoNumbers(self, l1, l2):
        rev_l1 = self.reverseList(l1)
        rev_l2 = self.reverseList(l2)
        count = 0
        ret = ListNode()
        tmp = ret
        while rev_l1 or rev_l2 or count:
            num = 0
            if rev_l1:
                num += rev_l1.val
                rev_l1 = rev_l1.next
            if rev_l2:
                num += rev_l2.val
                rev_l2 = rev_l2.next
            count, num = divmod(num + count, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return self.reverseList(ret.next)
```

```java []
class Solution {
    private ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode rev_l1 = this.reverseList(l1);
        ListNode rev_l2 = this.reverseList(l2);
        int count = 0;
        ListNode ret = new ListNode(0);
        ListNode cur = ret;
        while (rev_l1 != null || rev_l2 != null || count != 0) {
            int num = 0;
            if (rev_l1 != null) {
                num += rev_l1.val;
                rev_l1 = rev_l1.next;
            }
            if (rev_l2 != null) {
                num += rev_l2.val;
                rev_l2 = rev_l2.next;
            }
            num += count;
            count = num >= 10 ? 1 : 0;
            cur.next = new ListNode(num - count * 10);
            cur = cur.next;
        }
        return this.reverseList(ret.next);
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
