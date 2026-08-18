#my first solution 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len (sentence) < 26 : 
            return False 
        char_to_index = set()
        for value in sentence : 
            if value in char_to_index : 
                continue
            else : 
                char_to_index.add(value) 
        if len(char_to_index) == 26 :
            return True
        else : 
            return False 


#second with the perfect SET ever : 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len (sentence) < 26 : 
            return False 
        char_to_index = set(sentence)
        
        if len(char_to_index) == 26 :
            return True
        else : 
            return False 