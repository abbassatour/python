nums = [2, 7, 11, 15]
target = 9



class Solution: 
    def twoSum( self , nums : list[int]  , target : int ) -> list [int] :
        for  i , num in enumerate(nums ):
            for j in range ( i + 1  , len(nums)):
                if num + nums[j] == target :
                    return [i , j]
sol = Solution()

sol.towSum( target ,nums)