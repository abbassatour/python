# the brute force solution is going to take quadratic time

"""
Loop : 
    if max+ cur_num < 0 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = float('-inf')

        for i in nums: 
            cur_sum += i
            if cur_sum < 0 or cur_sum < i : 
                cur_sum = i 
            if max_sum < cur_sum : 
                max_sum = cur_sum
        return max_sum 

        '''
        -2 : cur = -2 , max = -2 
        1 : cur  = -1 => cur = 1 , max = 1
        -3 : cur = -2 => cur = -3 , max 1 
        4 : cur = 1 => cur = 1  , max = 1 
        -1 : cur = 0 => cur = 0 , max = 1 
        2 : cur = 2 , max = 2 : 
        1 : cur = 3 , max 3 
        -5 : cur= -2 => cur =-5 , max = 3 :
        4 : cur = -1  , max = 3
        
        '''