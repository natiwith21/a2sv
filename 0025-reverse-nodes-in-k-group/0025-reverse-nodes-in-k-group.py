class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start, end = head, head
        for _ in range(k):
            if not end: return head
            end = end.next
        
        # reverse diapason [start:end)
        def reverse(start, end):
            prev = None
            while start != end:
                start.next, start, prev = prev, start.next, start
            return prev # return head node of the reversed group
        
        newHead = reverse(start, end)
        start.next = self.reverseKGroup(end, k)

        return newHead