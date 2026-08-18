class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        n = 0 
        while n < len(nums): 
            if n not in numbers: 
                return n
            n+=1
        return len(nums)