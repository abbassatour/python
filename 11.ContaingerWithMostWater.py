#mine 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1

        bigest_container  = 0 
        while left < right : 
            if (right  - left ) * min (height[left] , height[right]) > bigest_container: 
                bigest_container = (right  - left ) * min (height[left] , height[right])
            
            if height[left] > height[right ] : 
                right -= 1
            elif  height[left] < height[right ] : 
                left += 1
            else : 
                if height [left + 1 ] >= height[right - 1 ] : 
                    right -= 1
                else :
                    left += 1
        return bigest_container

# Space Complexity: O(1) 
# Time Complexity: O(N)