#Wrong Solution 
#Learn English More to understand problems 
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        sorted_s = "".join(sorted(s))
        if sorted_s < target: 
            return sorted_s
        else :
            return ""