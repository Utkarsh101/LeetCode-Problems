class Solution():
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            # Getting middle node
            fast = slow = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
        
            # Reversing 2nd half of list
            prev = None
            while slow:
                curr = slow
                slow = curr.next
                curr.next = prev
                prev = curr
        
            # Merging 1st and 2nd half alternately 
            curr = head
            while prev:
                    next1 = curr.next
                    curr.next = prev 
                    next2 = prev.next
                    if next1:
                        prev.next = next1
                        curr = next1
                        prev = next2
                    else:
                        break