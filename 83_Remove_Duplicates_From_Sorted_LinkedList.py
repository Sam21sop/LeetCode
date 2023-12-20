class LinkedListNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    

    # This is optional function
    def createLinkedList(self, array_list):
        head = LinkedListNode()
        current = head
        if not array_list:
            return head
        for i in array_list:
            current.next = LinkedListNode(i)
            current = current.next
        return head.next
    

    # This is optional function
    def display(self, head):
        if not head:
            return
        current = head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print()
    

if __name__ == '__main__':
    arr_list = [1, 1, 2, 3, 3]
    object = Solution()
    head = object.createLinkedList(arr_list)
    object.display(head)
    sort_head = object.deleteDuplicates(head)
    object.display(sort_head)
