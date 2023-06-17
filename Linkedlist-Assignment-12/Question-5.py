# Given a linked list of **N** nodes such that it may contain a loop.

# A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

# Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
# Examples:
# Input:
# N = 3
# value[] = {1,3,4}
# X = 2
# Output:1
# Explanation:The link list looks like
# 1 -> 3 -> 4
#      ^    |
#      |____|
# A loop is present. If you remove it
# successfully, the answer will be 1.

# Input:
# N = 4
# value[] = {1,8,3,4}
# X = 0
# Output:1
# Explanation:The Linked list does not
# contains any loop.

# Input:
# N = 4
# value[] = {1,2,3,4}
# X = 1
# Output:1
# Explanation:The link list looks like
# 1 -> 2 -> 3 -> 4
# ^              |
# |______________|
# A loop is present.
# If you remove it successfully,
# the answer will be 1.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_and_remove_loop(head):
    slow = head
    fast = head
    loop_exists = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_exists = True
            break

    if not loop_exists:
        return head

    length = 1
    temp = slow.next
    while temp != slow:
        length += 1
        temp = temp.next

    ptr1 = head
    ptr2 = head
    for _ in range(length):
        ptr2 = ptr2.next

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr2.next != ptr1:
        ptr2 = ptr2.next

    ptr2.next = None

    return head


# Example 1
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = head1.next

result1 = detect_and_remove_loop(head1)
current = result1
while current:
    print(current.val, end=" ")
    current = current.next

# Example 2
head2 = ListNode(1)
head2.next = ListNode(8)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)

result2 = detect_and_remove_loop(head2)
current = result2
while current:
    print(current.val, end=" ")
    current = current.next

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = head3.next

result3 = detect_and_remove_loop(head3)
current = result3
while current:
    print(current.val, end=" ")
    current = current.next
