class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        before = head
        n = 0
        while n < left:
            before = before.next
            n += 1
        cur, pre = before, None
        while n < right:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n += 1
        before.next = pre
        return head
