#mine 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        right , left  = len(s) - 1 , 0
        while right > left :
            s[right] , s[left] = s[left] , s[right]
            right -= 1
            left += 1
