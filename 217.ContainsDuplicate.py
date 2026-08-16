#mine

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqe = set(nums)
        if len(uniqe) == len(nums) : 
            return False 
        else: 
            return True 