# pass in 48 ms

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
