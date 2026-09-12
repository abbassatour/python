# AI perfect for sliding windows
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If the character was seen inside the current window,
            # jump 'left' to the index right after the duplicate
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Update the character's latest index
            last_seen[char] = right

            # Current window length is always (right - left + 1)
            max_len = max(max_len, right - left + 1)

        return max_len



#my Bad Code 
#Solution 
#lengthOfLongestSubstring
"""
"a  b  c  a  b  c  b  b  p  w  w   k   e   w   a   b   c   d     p    e"
"1  2  3  4  5  6  7  8  9  10 11  13  14  15  16  17  18  19   20   21
 1  2  3  3  3  3  2  1  2  3   1   2   3   3   4   5   6   7    8    7
hash (char , last index we see the char at )
start_of_cur_uniq_sub  vs  last index we see the char at (the bigger win)
current uniq sub = index - winner 

loop : 
longest_uniq_sub

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_last_index = {}
        longest_uniq_sub = 0
        current_uniq_sub = 0
        start_of_cur_uniq_sub = 0 

        #"pwwkew"
        for index , char in enumerate(s):

            if char in chars_last_index:
                current_uniq_sub = index - max(chars_last_index[char] , start_of_cur_uniq_sub)
                chars_last_index[char] = index
                if chars_last_index[char] > start_of_cur_uniq_sub :
                    start_of_cur_uniq_sub = chars_last_index[char] + 1
                
            else : 
                current_uniq_sub  = index - start_of_cur_uniq_sub
                chars_last_index[char] = index

            longest_uniq_sub = max(longest_uniq_sub, current_uniq_sub ) 
        
        return longest_uniq_sub
             

#Mineeeeeeeeeeee
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        max_len = 0
        left = 0 
        last_seen = {}              
        
        for right , char in enumerate(s) : 
            
            if char in last_seen :
                left =  max(last_seen[char] + 1 , left)
            last_seen[char] = right 

            max_len = max(max_len, right - left )
            
        return max_len +1

        """
        a: 0 , 0  : max = 1 : last = {a:0}
        b: 0 , 1 : max = 2 : last = a:0  , b: 1 
        c: 0 , 2 : max = 3 : last  = a:0 ,b : 1 , c :2
        a: 1 , 3 : max = 3 : last = a:3 , b : 1 , c: 2 
        b: 2 , 4 : max = 3 : last =  a: 3, b: 4 , c: 2
        b: 5 , 5 : max = 3 : last = a: 3 , b: 5 , c : 2
        """