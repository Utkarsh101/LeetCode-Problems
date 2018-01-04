class Solution():
  def oddEvenList(self, head):
    
        try:  
          odd = head
          copy2 = even = head.next
        
          while odd.next:
            if odd == None:
                break
            odd.next = odd.next.next
            prev = odd
            odd = odd.next
            if even.next == None:
                break
            even.next = even.next.next
            even = even.next
            
          if odd:
            odd.next = copy2
          else:
            prev.next = copy2
          return head
    
        except:
          return None