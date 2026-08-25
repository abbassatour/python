#mine 
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 : 
            return True

        s1_list = list(s1) 
        s2_list = list(s2) 

        for index in range (2): 
            if s1_list[index] != s2_list[index] and s1_list[index] != s2_list[index+2]:
                return False
            if s1_list[index] != s2_list[index]: 
                s1_list[index] , s1_list[index+ 2] = s1_list[index + 2] , s1_list[index] 
        for index in range(4): 
            if s1_list[index] != s2_list[index] : 
                return False
        return True  