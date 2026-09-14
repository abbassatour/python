#AI 
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check X overlap: rec1's left is before rec2's right AND rec1's right is after rec2's left
        x_overlap = rec1[0] < rec2[2] and rec1[2] > rec2[0]
        
        # Check Y overlap: rec1's bottom is below rec2's top AND rec1's top is above rec2's bottom
        y_overlap = rec1[1] < rec2[3] and rec1[3] > rec2[1]
        
        return x_overlap and y_overlap