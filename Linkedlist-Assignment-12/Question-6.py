# Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

# Difficulty Level: Rookie

# Examples:
# Input:
# M = 2, N = 2
# Linked List: 1->2->3->4->5->6->7->8
# Output:
# Linked List: 1->2->5->6

# Input:
# M = 3, N = 2
# Linked List: 1->2->3->4->5->6->7->8->9->10
# Output:
# Linked List: 1->2->3->6->7->8

# Input:
# M = 1, N = 1
# Linked List: 1->2->3->4->5->6->7->8->9->10
# Output:
# Linked List: 1->3->5->7->9

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def retain_delete(head, M, N):
    if not head or M <= 0 or N <= 0:
        return head

    current = head
    count = 1

    while current:
        while current and count < M:
            current = current.next
            count += 1

        if not current:
            break

        temp = current.next
        for _ in range(N):
            if temp:
                temp = temp.next

        current.next = temp
        current = temp
        count = 0

    return head


# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)

result1 = retain_delete(head1, 2, 2)
current = result1
while current:
    print(current.val, end=" ")
    current = current.next

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
head2.next.next.next.next.next = ListNode(6)
head2.next.next.next.next.next.next = ListNode(7)
head2.next.next.next.next.next.next.next = ListNode(8)
head2.next.next.next.next.next.next.next.next = ListNode(9)
head2.next.next.next.next.next.next.next.next.next = ListNode(10)

result2 = retain_delete(head2, 3, 2)
current = result2
while current:
    print(current.val, end=" ")
    current = current.next

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
head3.next.next.next.next.next = ListNode(6)
head3.next.next.next.next.next.next = ListNode(7)
head3.next.next.next.next.next.next.next = ListNode(8)
head3.next.next.next.next.next.next.next.next = ListNode(9)
head3.next.next.next.next.next.next.next.next.next = ListNode(10)

result3 = retain_delete(head3, 1, 1)
current = result3
while current:
    print(current.val, end=" ")
    current = current.next
