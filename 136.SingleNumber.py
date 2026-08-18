#my first one 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_filter = set()
        for value in nums: 
            if value in num_filter:
                num_filter.remove(value)
            else: 
                num_filter.add(value)
        return num_filter.pop()

#the perfect mathematical one 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a ^=i
        return a