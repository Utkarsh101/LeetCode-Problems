class Solution:

    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = curr.next
            curr.next = prev
            prev = curr
        
        return prev