#mine
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        cur_sum = 0 

        for right in range(len(nums) ) :
            cur_sum += nums[right]

            while cur_sum >= target:

                if cur_sum - nums[left] >= target:
                    cur_sum -= nums[left]
                    left += 1

                else:
                    break
            
            if cur_sum >= target: 
                min_len = min(min_len , right - left)
                    
        if min_len == float('inf') : 
            return 0


        return min_len + 1
                


'''
[2,3,1,2,4,3]
2: min = 0 , l = 0 , r = 0, s = 2
3: min = 0 , l = 0 , r = 1, s = 5
1: min = 0 , l = 0 , r = 2, s = 6
2: min = 4 , l = 0 , r = 3, s = 8
4: min = 4 , l = 0 , r = 4, s = 12    =>    4: min: 3 , l = 2 , r = 4 , s = 7
3: min = 3 , l = 2 , r = 5 , s = 10    =>   3: min = 2 , l = 4 , r = 5 , s = 7
'''

# Time Complexity: O(N) linear
# Space Complexity: O(1) constant