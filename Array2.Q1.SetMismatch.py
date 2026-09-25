#mine
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        ans = []
        for i in nums:
            if i in seen: 
                ans.append(i)
                continue
            seen.add(i)
        for i in range(len(nums)):
            if i+1  not in seen:
                ans.append(i+1)
                return ans
            