#mine : the worse ever

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 , curr2  = list1 , list2 
        head = None 
        first_node = None
        if not curr1 and not curr2:
            return None 
        if not curr2: 
            return curr1 
        if not curr1 : 
            return curr2

        if curr1.val <= curr2.val:
                head = curr1
                curr1 = curr1.next
                first_node = head
        else : 
                head = curr2
                curr2 = curr2.next
                first_node = head

        while curr1 and curr2 : 
            if not curr1.next: 
                head.next = curr2
            if not curr2.next: 
                head.next = curr1

            if curr1.val < curr2.val:
                head.next = curr1
                curr1 = curr1.next
                head = head.next
            else:
                head.next = curr2
                curr2 = curr2.next
                head = head.next
        if curr1:
            head.next = curr1
        elif curr2:
            head.next = curr2
        return first_node 