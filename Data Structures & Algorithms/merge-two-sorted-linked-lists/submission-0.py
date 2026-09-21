# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = ListNode()
        current_node = ListNode()
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        current_node = head
    
        while list1 is not None or list2 is not None:
            if list1 is None:
                current_node.next = list2
                break
            elif list2 is None:
                current_node.next = list1
                break
            elif list1.val < list2.val:
                current_node.next = list1
                current_node = list1
                list1 = list1.next
            else:
                current_node.next = list2
                current_node = list2
                list2 = list2.next

        return head
        
        

        