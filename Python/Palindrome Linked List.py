class Solution():
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next        
            
        prev = None
        while slow:
            curr = slow
            slow = curr.next
            curr.next = prev
            prev = curr
            
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
            
        return True