class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = f'{x}'
        n = len(s) -1 
        for i in s :
            if i != s[n]:
                return False
            n-=1
        return True


#Edge Cases 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        s = f'{x}'
        n = len(s) -1 
        for i in s :
            if i != s[n]:
                return False
            n-=1
        return True

#for study 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy


class Solution:

    def isPalindrome(self, x: int) -> bool:
        # Guard Clause 1: Negative numbers are never palindromes (e.g., -121 -> 121-)
        # Guard Clause 2: Numbers ending in 0 (except 0 itself) are never palindromes (e.g., 10 -> 01)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Process and reverse only the second half of the digits
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10

        # For even number of digits: x == reversed_half (e.g., 1221 -> x=12, reversed_half=12)
        # For odd number of digits: x == reversed_half // 10 (e.g., 12321 -> x=12, reversed_half=123 -> 12)
        return x == reversed_half or x == reversed_half // 10