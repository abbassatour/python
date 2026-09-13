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

# Space Complexity = O(N.2^N)
# Time Complexity = O(N.2^N)
'''

No, the Big O analysis is not correct. Both the time and space complexity are
actually exponential (growing at an increasingly rapid rate), not polynomial
(O(N^2) or O(N^3)).

Notice the pattern in your own comments:

  - When len(nums) = 1 \rightarrow 2 subsets (2^1)
  - When len(nums) = 2 \rightarrow 4 subsets (2^2)
  - When len(nums) = 3 \rightarrow 8 subsets (2^3)

Every time you process a new number, you double the number of existing subsets.
For an input array of size N, the total number of subsets is always 2^N.

Here is the exact breakdown:

1. Time Complexity: O(N \cdot 2^N)

  - Number of subsets generated: There are 2^N total subsets.
  - Cost per subset: In the line subset.append(subset[i] + [num]), Python copies
    the elements of subset[i] to build the new list. A subset can have up to N
    elements (the average size of a subset is N / 2). Copying these elements
    takes O(N) time.
  - Multiplying the number of subsets by the copying cost gives:
    \mathcal{O}(N \cdot 2^N)

2. Space Complexity: O(N \cdot 2^N)

  - Output space: Your subset list holds all 2^N subsets. Since the average
    length of each subset is N / 2, storing them takes:
    \mathcal{O}(N \cdot 2^N) \text{ space}
  - Auxiliary space (extra space excluding the output): If an interviewer asks
    to ignore the memory used by the returned output, the auxiliary space is
    O(1) (or O(N) temporarily during the concatenation + [num]), because you are
    building the result in-place in that return list without using recursion
    call stacks or extra auxiliary data structures.

Key Takeaway

Whenever an algorithm involves generating all possible subsets (the power set),
combinations, or binary choices ("include" vs. "exclude"), the complexity will
almost always be tied to 2^N rather than powers of N like N^2 or N^3.

'''