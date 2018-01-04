class Solution():
  def oddEvenList(self, head):
    
        try:  
          copy1 = odd = head
          copy2 = even = head.next
        
          while odd.next:
            if odd == None:
                break
            odd.next = odd.next.next
            odd = odd.next
            if even.next == None:
                break
            even.next = even.next.next
            even = even.next
            
            
            
          while copy1.next:
            copy1 = copy1.next
          copy1.next = copy2 
        
          return head
    
        except:
          return None