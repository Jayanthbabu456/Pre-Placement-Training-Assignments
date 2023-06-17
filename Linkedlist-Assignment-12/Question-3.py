# Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

# Example 1:
# Input:
# N = 2
# LinkedList: 1->2->3->4->5->6->7->8->9
# Output:8
# Explanation:In the first example, there
# are 9 nodes in linked list and we need
# to find 2nd node from end. 2nd node
# from end is 8.

# Example 2:
# Input:
# N = 5
# LinkedList: 10->5->100->5
# Output:-1
# Explanation:In the second example, there
# are 4 nodes in the linked list and we
# need to find 5th from the end. Since 'n'
# is more than the number of nodes in the
# linked list, the output is -1.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_nth_from_end(head, n):
    main_ptr = head
    ref_ptr = head

    for _ in range(n):
        if not ref_ptr:
            return -1
        ref_ptr = ref_ptr.next

    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    if not main_ptr:
        return -1

    return main_ptr.val


# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)
head1.next.next.next.next.next.next.next.next = ListNode(9)

result1 = find_nth_from_end(head1, 2)
print(result1)


# Example 2
head2 = ListNode(10)
head2.next = ListNode(5)
head2.next.next = ListNode(100)
head2.next.next.next = ListNode(5)

result2 = find_nth_from_end(head2, 5)
print(result2)

