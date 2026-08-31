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

#AI 
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        # Guard clause (early exit condition): Critical points require at least 3 nodes
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        curr_idx = 1

        while curr.next:
            # Self-documenting condition checks
            is_local_max = curr.val > prev.val and curr.val > curr.next.val
            is_local_min = curr.val < prev.val and curr.val < curr.next.val

            if is_local_max or is_local_min:
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_idx)
                
                prev_idx = curr_idx

            # Advance pointers
            prev = curr
            curr = curr.next
            curr_idx += 1

        # If fewer than 2 critical points were found
        if first_idx == prev_idx:
            return [-1, -1]

        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]