class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        uniq_fast = set(nums)
        uniq_nums = sorted(uniq_fast)
        
        longest_consecutive = 0 

        cur_sequence = 1
        for index , value in enumerate(uniq_nums): 

            if uniq_nums[index - 1] == value -1: 
                cur_sequence +=1
            else : 
                if longest_consecutive < cur_sequence: 
                    longest_consecutive = cur_sequence 
                cur_sequence = 1

        if longest_consecutive < cur_sequence: 
            longest_consecutive = cur_sequence

        return longest_consecutive  

#Time Complexity : O(N+Ulog(U))--> O(Ulog(U))
#wrong drop: we Cant drop the N here because of edge cases  
#Space Complexity :  O(2U) --> O(U)