# Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
# **Examples:**

#  Input: R->A->D->A->R->NULL
 
 
#  **Output:** Yes
 
#  **Input:** C->O->D->E->NULL
 
#  **Output:** No

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    def reverse_linked_list(node):
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_linked_list(slow)

    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# Example 1
head1 = ListNode('R')
head1.next = ListNode('A')
head1.next.next = ListNode('D')
head1.next.next.next = ListNode('A')
head1.next.next.next.next = ListNode('R')

result1 = is_palindrome(head1)
print(result1)


# Example 2
head2 = ListNode('C')
head2.next = ListNode('O')
head2.next.next = ListNode('D')
head2.next.next.next = ListNode('E')

result2 = is_palindrome(head2)
print(result2)

