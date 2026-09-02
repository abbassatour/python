class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        uni_nums = set()
        #checking all rows: 
        for i in board: 
            for j in i : 
                if j in uni_nums: 
                    return False
                if j != ".": 
                    uni_nums.add(j)
            uni_nums.clear()
        
        #checking all columns: 
        for i in range(9):
            for j in range(9):
                if board[j][i] in uni_nums: 
                    return False 
                if board[j][i] != ".": 
                    uni_nums.add(board[j][i])
            uni_nums.clear()


        #checking  all sub-boxes: 
        for i in range(0 , 9 , 3): 
            for j in range (0 , 9 , 3) : 
                for k in range(i , i+3):
                    for l in range(j , j+3): 
                        if board[k][l] in uni_nums: 
                            return False 
                        if board[k][l] != ".": 
                            uni_nums.add(board[k][l])
                uni_nums.clear()        

        return True

#Space Complexity : O(9 ) --> O(1)
#Time Complexity : O(81 + 81 + 81 ) --> O(1)