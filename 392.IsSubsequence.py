class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: 
            return True 
        index = 0
        for char in t: 
            if char == s[index] :
                index +=1
            if index == len(s) : 
                return True 
        return False
    #time complexity : O(1)
    #Space Complexity : O(1)