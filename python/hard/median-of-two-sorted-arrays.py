# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            return (nums[n//2] + nums[n//2-1])/2
        else:
            return nums[n//2]