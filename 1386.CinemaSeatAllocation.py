#Time Limit Exceeded
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        groups_num = 0
        set_reserved  = set(map(tuple , reservedSeats))

        for i in range( n   , 0  , -1):
            skip_last  = 0
            for m in range (2 , 6): 

                if (i , m ) in set_reserved : 
                    break
                if m == 5: 
                    groups_num+=1
                    skip_last = 1
            for m in range( 6 , 10 ) : 

                if (i , m ) in set_reserved: 
                    break
                if m == 9:
                    groups_num += 1 
                    skip_last = 1 

            if skip_last == 0 : 
                for m in range (4 , 8 ) : 
                    if (i , m ) in set_reserved: 
                        break 
                    if m == 7: 
                        groups_num += 1 

        return groups_num 

#my improbed code 
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        set_reserved  = set(map(tuple , reservedSeats))
        only_reserved_rows = set()
        for i , _ in set_reserved : 
            only_reserved_rows.add(i)
        
        groups_num = 2 *(n - len( only_reserved_rows) )

        for i in only_reserved_rows : 
            skip_last = 0 
            for m in range(2 , 6) : 
                if (i, m ) in set_reserved: 
                    break
                if m == 5: 
                    groups_num += 1
                    skip_last = 1

            for m in range(6 , 10 ) : 
                if ( i , m ) in set_reserved: 
                    break
                if m == 9 : 
                    groups_num += 1
                    skip_last = 1
            
            if skip_last == 0 : 
                for m in range(4 , 8) : 
                    if (i , m) in set_reserved: 
                        break
                    if m == 7: 
                        groups_num += 1
            
        return groups_num 