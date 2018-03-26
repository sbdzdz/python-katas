def detect_cycle(head):
    seen = set()
    current = head
    while current.next is not None:
        if current in seen:
            return current
        seen.add(current)
        current = current.next
