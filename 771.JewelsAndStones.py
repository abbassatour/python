#mine
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        h = {}
        num = 0
        for i in jewels:
            if i not in h:
                h[i] = 0
        for i in stones:
            if i in h :
                num += 1
        return num 