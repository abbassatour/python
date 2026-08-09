#Mine
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max  = 0 

        for i in accounts:
            current = 0
            for m in i:
                current += m
            if current > max: 
                max = current
        return max

#perfect
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth

#more than perfect , to study 
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)