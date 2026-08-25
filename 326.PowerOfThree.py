#Tons of errors 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 : 
            return True
        if n < 3 : 
            return False 
        while n > 3 : 
            if n % 3 != 0 : 
                return False
            n = n / 3

        if n !=3: 
            return False
        return True 