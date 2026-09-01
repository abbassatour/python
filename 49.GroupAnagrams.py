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
        #Time Complexity : O(N^2Mlog(M))
        #Space Complexity : O(NM)

#decumenting : 
#Mine : 
# 1 storing every element in a hash map where the value is an array of strings which have the same charactars and the key of the hash map will be the sorted string of every element it contains 

        #2 itrate on every element and see if its sorted version in the hash map then if its or not we have to conditions to dell with 
        # first if it was we will add it to the array
        # second if it wasnt we weill create new pair in the hash map for it 



#AI:
# Approach: Hash Map (Anagram Grouping)
# - Key: Sorted string (canonical form)
# - Value: List of matching anagrams
# - Iterate through strs -> insert into map
# - Return map.values()
# Time: O(N * K log K), Space: O(N * K)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_anagrams = {}
        for i in strs :
            hash_anagrams.setdefault("".join(sorted(i)), []).append(i)
            #incorrect : hash_anagrams.get(["".join(sorted(i))],[]).append(i)
            #incorrect : hash_anagrams["".join(sorted(i))] = get(hash_anagrams["".join(sorted(i))], []).append(i) 
            #incorrect : hash_anagrams["".join(sorted(i))] = hash_anagrams.get(["".join(sorted(i))], []).append(i)

        return list(hash_anagrams.values())
    