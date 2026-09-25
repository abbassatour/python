#mine
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        smaller_nums = {}
        for i in range(len(sorted_nums) ): 
            if sorted_nums[i] not in smaller_nums: 
                smaller_nums[sorted_nums[i]] = i
        ans = []
        for i in nums: 
            ans.append(smaller_nums[i]) 
        return ans

#Time Complexity: O(N*logN + N + N) => O(N*logN)
#Space Complexity: O(N + N + N) => O(N)