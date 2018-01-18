'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

class Solution():
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        aplh = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in aplh if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
                
                
                
        

