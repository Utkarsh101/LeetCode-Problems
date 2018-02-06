'''
Given an integer, write a function to determine if it is a power of three.
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n % 3 == 0 and n != 0:
            n = n/3
        return True if n == 1 else False    
        