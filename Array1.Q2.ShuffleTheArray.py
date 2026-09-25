mine
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n): 
            ans.append(nums[i])
            ans.append(nums[n])
            n+= 1 
        return ans