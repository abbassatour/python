class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) * 2):
            if i < len(nums): 
                ans.append(nums[i])
            else:
                ans.append(nums[i - len(nums)])

        return ans 

'''
[1,2,1] n: 3
i   ans     
0   [1]
1   [1, 2]
2   [1, 2, 1]
3   [1, 2, 1, 1]
4   [1, 2, 1, 1, 2]
5   [1, 2, 1, 1, 2, 1]
'''

