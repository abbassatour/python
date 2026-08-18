#mine 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        n = 0 
        while n < len(nums): 
            if n not in numbers: 
                return n
            n+=1
        return len(nums)

#more pythonic way
# Instead of:
# n = 0
# while n < len(nums):
#     if n not in numbers:
#         return n
#     n += 1

# More Pythonic:
for num in range(len(nums) + 1):
    if num not in numbers:
        return num