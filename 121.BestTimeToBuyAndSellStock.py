class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max_profit , max_price 
        #start from the end storing and updating poth on every element we enter 
        max_profit = 0
        max_price = 0
        
        for i  in range(len(prices)-1 , -1, -1): 
            max_price = max(max_price , prices[i]) 
            max_profit = max(max_profit , max_price - prices[i]  )

        return max_profit 
        #time complexity  = O(N) 
        #Space Complexity = O(1)

        # [ 7 , 1 , 5 , 3 , 6 , 4 ]
        # 4:  max_price = 4 , max_profit = 0 
        # 6: max_price =  6, max_profit =  0 (6 - 6 ) 
        # 3: max_price = 6 , max_profit = 3 ( 6 - 3 ) 
        # 5: max_price = 6 , max_profit = 3 (6 - 5 , 3) 
        # 1: max_price = 6 , max_profit = 5 (6 - 1 , 3) 
        # 7: max_price = 7 , max_profit =  5 (7 -7  , 5) 


        #1 : max_price  = 1 max_profit = 0 
        #2