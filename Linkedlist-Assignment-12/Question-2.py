# Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

# **Example 1:**
# Input:
# N = 3
# value[] = {1,3,4}
# x(position at which tail is connected) = 2
# Output:True
# Explanation:In above test case N = 3.
# The linked list with nodes N = 3 is
# given. Then value of x=2 is given which
# means last node is connected with xth
# node of linked list. Therefore, there
# exists a loop.

# Example 2:
# Input:
# N = 4
# value[] = {1,8,3,4}
# x = 0
# Output:False
# Explanation:For N = 4 ,x = 0 means
# then lastNode->next = NULL, then
# the Linked list does not contains
# any loop.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Example 1
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = head1.next

result1 = has_loop(head1)
print(result1)


# Example 2
head2 = ListNode(1)
head2.next = ListNode(8)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)

result2 = has_loop(head2)
print(result2)

