#my stubid solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counter = {} 
        for index , value in enumerate(t) :
            if value in     char_counter: 
                char_counter[value] += 1
            else:
                char_counter[value] = 1
        char_counter2 = {} 
        for index , value in enumerate(s) :
            if value in     char_counter2: 
                char_counter2[value] += 1
            else:
                char_counter2[value] = 1
        if char_counter == char_counter2 : 
            return True
        else: 
            return False 

#cleaner code 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not  len(s)  == len(t):
            return False 
        count_t = {} 
        for char in t: 
            if char in count_t: 
                count_t[char] += 1 
            else : 
                count_t[char] = 1

        count_s = {}
        for char in s: 
            if char in count_s: 
                count_s[char] += 1 
            else : 
                count_s[char] = 1
        
        return count_s == count_t