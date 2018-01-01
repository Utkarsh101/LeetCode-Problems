class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
                
        while head:
            curr = head
            if head.val == val:
                head = head.next
                
            else:
                head = head.next
                curr.next = prev
                prev = curr
                
        head = prev
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev