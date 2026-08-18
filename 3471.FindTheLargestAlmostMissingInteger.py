#my bad solution
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1 :
            hash_map = {}
            for i in nums:
                hash_map[i] = hash_map.get(i , 0) +1
            largest_num = -1
            for num , count in hash_map.items(): 
                if count == 1 : 
                    if largest_num < num: 
                        largest_num = num
            return largest_num

        
        elif k == len(nums):
            unique_num= set(nums)
            largest_num = -1
            for i in unique_num: 
                if largest_num < i : 
                    largest_num = i 
            return largest_num 


        
        else :
            last_item = nums[len(nums) -1]
            first_item = nums[0]
            if first_item == last_item :
                return -1
            for i in range(1 , len(nums)-1) : 
                if nums[i] == last_item:
                    last_item = -1
                elif nums[i ]== first_item: 
                    first_item =-1 
            res = max(first_item , last_item) 
            return res 

#the perfect way 

from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Case 1: Subarrays of size 1 (Find largest number with frequency == 1)
        if k == 1:
            counts = Counter(nums)
            unique_candidates = [num for num, count in counts.items() if count == 1]
            return max(unique_candidates, default=-1)

        # Case 2: Subarray is the entire array (Every number appears in exactly 1 window)
        if k == len(nums):
            return max(nums)

        # Case 3: 1 < k < len(nums) (Only the two endpoints can appear in exactly 1 window)
        first_num = nums[0]
        last_num = nums[-1]
        
        result = -1
        if nums.count(first_num) == 1:
            result = max(result, first_num)
        if nums.count(last_num) == 1:
            result = max(result, last_num)

        return result

    