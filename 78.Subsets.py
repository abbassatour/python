class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums: 
            for i in range(len(subset) -1, -1 , -1):
                subset.append(subset[i] + [num])
                

        return subset

# 1: sub = [[], [1]]
# 2: sub = [[], [1], [2], [1, 2]]
# 3: sub = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
