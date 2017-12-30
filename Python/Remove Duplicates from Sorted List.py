# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        else:
            prev = head
            curr = head.next
        
            while curr:
                if prev.val == curr.val:
                    prev.next = curr.next
                    curr = curr.next
                
                else:
                    prev = curr
                    curr = curr.next
        
        return head