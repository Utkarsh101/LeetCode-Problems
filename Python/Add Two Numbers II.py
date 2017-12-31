class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2): return l1 or l2
        # reverse lists:
        r1,r2 = self._rev(l1),self._rev(l2)
        # regular addition
        r = self._add(r1,r2)
        # return reversed regular addition
        return self._rev(r)
        
    def _rev(self, head):
        prev = None
        
        while head:
            curr = head
            head = curr.next
            curr.next = prev
            prev = curr
        
        return prev
    
    def _add(self, l1, l2):
        if not (l1 and l2): return l1 or l2
        tot = l1.val+l2.val
        val,carry = tot if tot<10 else tot-10,0 if tot<10 else 1
        new = ListNode(val)
        new.next = self._add(l1.next, l2.next) if not carry else self._add(self._add(l1.next,l2.next), ListNode(1))
        return new