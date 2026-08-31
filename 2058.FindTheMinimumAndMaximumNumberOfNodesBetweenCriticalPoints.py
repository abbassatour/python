#my solution 
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        max_dis = 0
        min_dis = 10** 5 
        
        prev_val = head.val
        head = head.next
        first_point = 0 
        curr_dis = 0
        longest_dis =0
        first_critical = False
        while head:
            if not head.next:
                break

            if first_critical: 
                curr_dis +=1 
                longest_dis +=1

            curr_val = head.val
            next_val = head.next.val 

            if curr_val> prev_val and curr_val>next_val or curr_val<prev_val and curr_val< next_val :
                if first_critical:
                    if max_dis< longest_dis:
                        max_dis = longest_dis
                    if min_dis > curr_dis : 
                        min_dis = curr_dis
                    curr_dis = 0
                first_critical = True 

            prev_val = head.val
            head = head.next
             


        if max_dis == 0 : 
            return [-1 , -1]
            
        return [min_dis, max_dis]

            
        