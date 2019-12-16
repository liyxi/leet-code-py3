# pass in 48 ms

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, v in enumerate(nums):
            d[v] = k
            
        for i, x in enumerate(nums):
            cand = target - x
            j = d.get(cand)
            if j and i!=j:
                return i, j
