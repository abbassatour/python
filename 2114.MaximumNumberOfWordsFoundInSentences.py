#perfect one liner 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=max(len(s.split(' ')) for s in sentences)
        return max_words

#mine 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount = 0
        for i in sentences:
            counter = 0
            for l in i :
                if l == ' ': 
                    counter +=1
            if counter > maxCount:
                maxCount = counter
        return maxCount + 1