class Solution(object):
        
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        try:  
          def rev(hnode):
            rev.prev = None
            while hnode:
                curr = hnode
                hnode = curr.next
                curr.next = rev.prev
                rev.prev = curr
                
            return rev.prev    
            
          rev(head)
        
          prev2 = rev.prev
          if n > 1:
            count = 1
            while count < n:
              prev3 = prev2
              prev2 = prev2.next
              count += 1
            
            prev3.next = prev2.next
            return rev(rev.prev)
          else:
            prev2 = prev2.next
            return rev(prev2)
        
        except:
            return