# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        return head.next
    


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    obj = Solution()
    head = obj.mergeTwoLists(list1, list2)
    