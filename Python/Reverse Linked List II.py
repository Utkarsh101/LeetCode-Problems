class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        curr = head
        count = 1
        while count < m:
            prev = head
            head = head.next
            count += 1
        
        count = 0
        prev2 = None
        while count <= (n-m):
            curr2 = head
            head = curr2.next
            curr2.next = prev2
            prev2 = curr2
            count += 1
            
        if m!= 1:
            prev.next = prev2
        elif m == 1:
            prev3 = prev2
        
        while prev2.next:
            prev2 = prev2.next
            
        prev2.next = head
        
        if m == 1:
            return prev3
        else:
            return curr