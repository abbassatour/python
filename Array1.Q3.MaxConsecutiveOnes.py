#my stupid solution 
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_con = 1 if nums[0] == 1 else 0
        cur_con = max_con
        for i in range(1, len(nums)):
            if nums[i -1] == 1 and nums[i] ==1: 
               cur_con += 1
            elif nums[i] == 1:
                cur_con = 1
            max_con = max(max_con , cur_con)
        return max_con


#AI solution
class Solution:

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_con = 0
        cur_con = 0

        for num in nums:
            if num == 1:
                cur_con += 1
                max_con = max(max_con, cur_con)
            else:
                cur_con = 0

        return max_con