#AI 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n % 3 == 1)

#normal loop 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        complications = set()
        for i in range(16): 
            complications.add(4** i)
        
        return  n in complications

#Naming Correctly and comments 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Time Complexity:  O(1) - The loop runs a fixed number of times (16 iterations).
        Space Complexity: O(1) - The set stores a fixed maximum of 16 integers.
        """
        # A 32-bit signed integer ranges up to 2^31 - 1 (~2.14 * 10^9).
        # The largest power of 4 within this range is 4^15 (2^30).
        powers_of_four = set()
        for i in range(16):
            powers_of_four.add(4 ** i)
        
        # Set lookup in Python operates in O(1) average time complexity
        return n in powers_of_four


#more direct : 
class Solution:
    # Time: O(1) | Space: O(1)
    def isPowerOfFour(self, n: int) -> bool:
        # 4^15 is the maximum power of 4 that fits in a 32-bit signed integer
        return n in {4 ** i for i in range(16)}

#recursion
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0 :
            return False
        if n ==1: 
            return True
        
        return  self.isPowerOfFour(n/4)
