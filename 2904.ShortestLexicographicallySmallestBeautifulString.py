#mine
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones  = []
        for index  in range(len(s)) : 
            if s[index] == '1': 
                ones.append(index)
        if len(ones) < k: 
            return "" 
        shortest_beutiful_substring = 100
        start = 0
        end = len(s) - 1
        for index in range(len(ones)- k + 1):
            if ones[index + k - 1] - ones[index] < shortest_beutiful_substring:
                shortest_beutiful_substring = ones[index + k - 1] - ones[index]
                start = ones[index]
                end = ones[index + k - 1]
                continue
            if ones[index + k - 1] - ones[index] == shortest_beutiful_substring:
                if s[start : end + 1] > s[ones[index] : ones[index + k - 1]]:
                    start = ones[index]
                    end = ones[index + k - 1]
        return s[start : end + 1]