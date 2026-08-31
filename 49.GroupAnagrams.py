#my brute force solution: 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagrams_list = []
        for index , value in enumerate(strs) : 
            if value == '-1' : 
                continue 
            anagrams_list.append([value])
            for j in range(index+ 1, len(strs) ):
                if sorted(value) == sorted(strs[j]) or strs[j] == '' and value == '' : 
                    anagrams_list[-1].append(strs[j]) 
                    strs[j] = '-1'
                
        return anagrams_list