#Brute Force
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counter = 0 
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]  + nums[j] < target : 
                    counter += 1 
        return counter 



#My ingenious solution
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        d = {} 
        for i , v in enumerate(nums):
            if v in d: 
                d[v] += 1 
            else :
                d[v] = 1 
        l = sorted(set(nums))
        
        left , right = 0 , len(l) - 1
        count = 0 

        while left < right :
            if l[left] + l[right] >= target:
                right -= 1
                continue
            else :
                count += d[l[left]] * d[l[right]]
                left += 1
        return count


#AI 
from collections import Counter

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        # Guard clause: edge case where no pairs can exist
        if len(nums) < 2:
            return 0
        
        freq = Counter(nums)
        unique = sorted(freq.keys())
        
        total_pairs = 0
        left = 0
        right = len(unique) - 1
        
        while left <= right:
            if left == right:
                if unique[left] * 2 < target:
                    f = freq[unique[left]]
                    total_pairs += (f * (f - 1)) // 2
                break
            
            if unique[left] + unique[right] < target:
                range_freq_sum = sum(freq[unique[k]] for k in range(left + 1, right + 1))
                total_pairs += freq[unique[left]] * range_freq_sum
                if unique[left] * 2 < target:
                    f = freq[unique[left]]
                    total_pairs += (f * (f - 1)) // 2
                
                left += 1
            else:
                right -= 1
                
        return total_pairs


#Perfect AI 
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
                
        return count