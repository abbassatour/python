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