# Given a singly linked list, find if the linked list is circular or not.

#  A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_circular(head):
    if not head or not head.next:
        return False

    tortoise = head
    hare = head.next

    while hare and hare.next:
        if tortoise == hare:
            return True

        tortoise = tortoise.next
        hare = hare.next.next

    return False


# Example 1: Circular linked list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = head1

result1 = is_circular(head1)
print(result1)

# Example 2: Non-circular linked list
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)

result2 = is_circular(head2)
print(result2)
