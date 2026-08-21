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

#without recursion
class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0 , 1 , 1 ] 
        if n < 3 : 
            return T[n]
        for index in range(3 , n + 1) : 
            T.append( T[index - 1] + T[index - 2] + T[index - 3 ] )
        return T[n]
