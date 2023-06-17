# Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
# For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

# Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists(head1, head2):
    if not head2:
        return head1

    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        next1 = curr1.next

        curr1.next = curr2
        curr2 = curr2.next
        curr1.next.next = next1

        curr1 = next1

    return head1, head2


# Example 1
head1 = ListNode(5)
head1.next = ListNode(7)
head1.next.next = ListNode(17)
head1.next.next.next = ListNode(13)
head1.next.next.next.next = ListNode(11)

head2 = ListNode(12)
head2.next = ListNode(10)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(6)

result1, result2 = merge_lists(head1, head2)

current = result1
while current:
    print(current.val, end=" ")
    current = current.next

current = result2
while current:
    print(current.val, end=" ")
    current = current.next

# Example 2
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)

head4 = ListNode(4)
head4.next = ListNode(5)
head4.next.next = ListNode(6)
head4.next.next.next = ListNode(7)
head4.next.next.next.next = ListNode(8)

result3, result4 = merge_lists(head3, head4)

current = result3
while current:
    print(current.val, end=" ")
    current = current.next

current = result4
while current:
    print(current.val, end=" ")
    current = current.next
