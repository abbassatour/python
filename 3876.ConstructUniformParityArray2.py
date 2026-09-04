#mine
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum_odd = 10**9 +1
        minimum_even = 10 **9 +1
        for val in nums1: 
            if val % 2 == 0: 
                minimum_even = min(minimum_even , val)
            else:
                minimum_odd = min (minimum_odd , val)

        if minimum_odd > minimum_even and minimum_odd != 10**9 +1 : 
            return False
        return True
#Space Complexity : O(1)
#Time Complexity : O(N)