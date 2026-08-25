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

#Recursion
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 : 
            return True
        if n < 3 : 
            return False 
        
        if n % 3 != 0 : 
            return False
        
        
        return self.isPowerOfThree(n // 3)

#AI Perfect 
# Analogous Example: Checking for powers of 5
class PowerChecker:
    def is_power_of_five(self, val: int) -> bool:
        # Guard clause 1: Reject non-positive domain
        if val <= 0:
            return False
        
        # Base case: Terminal power (5^0 == 1)
        if val == 1:
            return True
        
        # Guard clause 2: Check divisibility
        if val % 5 != 0:
            return False
        
        # Recursive step with integer division
        return self.is_power_of_five(val // 5)