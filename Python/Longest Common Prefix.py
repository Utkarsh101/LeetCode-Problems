'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:

    def lcp(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]

    # @return a string                                                                                                                                                          
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp,strs)