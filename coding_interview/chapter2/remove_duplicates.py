from linked_list import *

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    seen = set([head.value])
    current = head
    while current.next is not None:
        if current.next.value in seen:
            duplicate = current.next
            while duplicate is not None and duplicate.value in seen:
                duplicate = duplicate.next
            current.next = duplicate
        if current.next is not None:
            seen.add(current.next.value)
            current = current.next
    return head

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    seen = set()
    current = head
    while current is not None:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    return head
