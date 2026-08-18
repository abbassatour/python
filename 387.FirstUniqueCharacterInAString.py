#my solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uni_char = {}
        for index , value in enumerate(s) : 
            if value in uni_char: 
                uni_char[value ] =-1 
            else :
                uni_char[value ] = index 
        
        for i in uni_char.values():
            if i != -1 :
                return i 
        
        return -1 
            
        
# Could you rewrite my code using ideal naming conventions
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1. Guard Clause for boundary condition
        if len(s) == 1:
            return 0

        # 2. Descriptive Hash Map (maps character -> first index or -1)
        char_indices = {}

        # 3. First pass: record first seen index or mark duplicates with -1
        for index, char in enumerate(s):
            if char in char_indices:
                char_indices[char] = -1
            else:
                char_indices[char] = index

        # 4. Second pass: find the first non-duplicate index in insertion order
        for idx in char_indices.values():
            if idx != -1:
                return idx

        return -1