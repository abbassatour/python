#Time Limit Exceeded
class Solution:
    def tribonacci(self, n: int) -> int:
        t0 , t1  , t2 = 0 ,1 , 1
        if n <= 1 : 
            return n 
        
        if n == 2 : 
            return 1

        n  = self.tribonacci(n-1) + self.tribonacci(n - 2 ) + self.tribonacci(n - 3)

        return n

