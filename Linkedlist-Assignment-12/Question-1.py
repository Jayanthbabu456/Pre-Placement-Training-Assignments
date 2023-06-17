# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL
# Example 1:
# Input:
# LinkedList: 1->2->3->4->5
# Output:1 2 4 5
# Example 2:
# Input:
# LinkedList: 2->4->6->7->5->1
# Output:2 4 6 5 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle_node(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return head


# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

result1 = delete_middle_node(head1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next


print()

# Example 2
head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)
head2.next.next.next = ListNode(7)
head2.next.next.next.next = ListNode(5)
head2.next.next.next.next.next = ListNode(1)

result2 = delete_middle_node(head2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next

