class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(0 , n) :
            arr.append(nums[i])
            arr.append ( nums[n])
            n+=1
        return arr

#to study zip 
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [item for pair in zip(nums[:n], nums[n:]) for item in pair]