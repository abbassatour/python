#my stupid solution 
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        #after doing this we need to find a way to extract the most frequent numbers :
        most_freq = []
        for i in freq: 
            most_freq.append([i.value, i.key])
        sorted_freq = sorted(most_freq)
        j = len(sorted_freq) -1
        res = []
        while k > 0: 
            res.append(sorted_freq[j][1])
            j-=1
            k-=1
        return res 
# you cant iterate on a hash map using this way 



#the correct solution with Big(O) Tips 


from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        #after doing this we need to find a way to extract the most frequent numbers :
        most_freq = []
        for key , value in freq.items(): 
            most_freq.append([value, key])

        sorted_freq = sorted(most_freq)
        j = len(sorted_freq) -1
        res = []
        while k > 0: 
            res.append(sorted_freq[j][1])
            j-=1
            k-=1
        return res 

#Space Complexity : O(2U+K)  --> O(U)
#Time Complexity : O(N+U+ Ulog(U) +K)  --> O(N+UlogU)



'''

Step-by-Step Simplification

1.  Compare k vs. U:

      - Since k \le U (you can't pick more top elements than the total unique
        elements), the U term dominates k. So + k is dropped.

2.  Compare U vs. U \log U:

      - U \log U grows much faster than U. Therefore, U \log U dominates U, and
        \+ U is dropped.

3.  Compare N vs. U \log U:

      - N represents the total elements in nums.
      - U represents the unique elements (1 \le U \le N).
      - Because N and U scale independently depending on duplicate frequency, we
        keep both.

Final Time Complexity

\mathbf{O(N + U \log U)}

  - Worst-case scenario (all elements are unique, meaning U = N):
    O(N + N \log N) \rightarrow \mathbf{O(N \log N)}
  - Best-case scenario (very few unique elements, U \ll N): The N term prevails
    (remains the main one), so the complexity is nearly linear: \mathbf{O(N)}.

Space Complexity Check

Your space analysis is spot on: O(2U + k) \rightarrow \mathbf{O(U)} (Since U
unique elements are stored in the Counter and the most_freq list, and k \le U.)

[Feedback]

  - Word Choice / Phrasing: Instead of saying "do the time complexity's sum", it
    is more natural to say "simplify the time complexity" or "calculate the
    total time complexity".

'''