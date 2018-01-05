'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1]
'''

class Solution():
    
  def searchRange(self, nums, target):
    lo = bisect.bisect_left(nums, target)
    return [lo, bisect.bisect_left(nums, target+1)-1] if target in nums[lo:lo+1] else [-1, -1]