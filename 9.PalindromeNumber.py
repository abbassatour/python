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