class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:        
        return nums  + nums 


#for study 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums 
        for i in nums :
            arr.append(i)
        return arr