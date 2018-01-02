class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        if l1 is None or l2 is None:
            return l1 or l2
            
        tot = l1.val+l2.val
        val, carry = tot if tot<10 else tot-10, 0 if tot<10 else 1  
        res = ListNode(val)
        res.next = self.addTwoNumbers(l1.next, l2.next) if not carry else self.addTwoNumbers(ListNode(1),self.addTwoNumbers(l1.next, l2.next))
        return res