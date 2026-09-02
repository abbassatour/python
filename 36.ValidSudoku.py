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


#professional way of typing 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check Rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # 2. Check Columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # 3. Check 3x3 Sub-boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = set()
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True

    