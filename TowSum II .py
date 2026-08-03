#0ms
class Solution:
    def twoSum ( self, numbers :List[int], target :int )->List[int]:
        right =  len(numbers) - 1 
        left = 0
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:  
                right -= 1
            else:
                left += 1

#3ms
class Solution:
    def twoSum ( self, numbers :List[int], target :int )->List[int]:
        right =  len(numbers) - 1 
        left = 0
        while left < right :
            if numbers[right] + numbers[left] == target :
                return [left  +1, right  +1] 
            elif numbers[right]   + numbers[left ] > target:
                right-=1
            elif numbers [right] + numbers [left ] < target :
                left +=1