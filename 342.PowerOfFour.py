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



#recursion
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0 :
            return False
        if n ==1: 
            return True
        
        return  self.isPowerOfFour(n/4)
