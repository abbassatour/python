class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_num = -1 

        for index , num in enumerate(nums) : 
            min_num = float('inf')
            max_num = max(max_num , num )
            
            for j in range(index + 1 , len(nums)): 
                min_num = min(min_num  , nums[j])
            if max_num - min_num <= k:
                return index

        return -1

#Space Complexity : O(1)
#Time Complexity : O(N^2)


# Explain the Approach :

'''
For this initial approach, I’m using a straightforward two-pointer / nested loop 
strategy. As I iterate through the array, I maintain a running maximum for the
prefix. For every index, I scan the rest of the array to find the minimum value
in the suffix, and then I check if the difference is within k.
'''

# Time and space complexity : 
'''
Time Complexity: It's O(N^2) The outer loop runs N times, and for each element,
 the inner loop scans up to N remaining elements. That results in approximately
 (N^2 / 2) operations in the worst case, which simplifies to quadratic time

Space Complexity: It's O(1) auxiliary space because we only store a couple of 
primitive variables to track the minimum and maximum values without allocating 
any extra data structures
'''

# Transition Proactively : 

'''
This brute-force approach works and uses constant extra space, but the 
quadratic time complexity might be a bottleneck for larger inputs. I can 
look into optimizing the time complexity if you'd like
'''


