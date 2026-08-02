nums = [2, 7, 11, 15]
target = 9


'''
class Solution: 
    def twoSum( self , nums : list[int]  , target : int ) -> list [int] :
        for  i , num in enumerate(nums ):
            for j in range ( i + 1  , len(nums)):
              if num + nums[j] == target :
                print([i , j])
                return [i , j]
'''            


class Solution: 
    def twoSum( self , nums : list[int]  , target : int ) -> list [int] :
        hash= {}
        for i , num in enumerate(nums):
            if target -num  in hash:
                return [i , hash[target- num]]
            hash[num ] =i 
    

                    
sol = Solution()

sol.twoSum( nums ,target)