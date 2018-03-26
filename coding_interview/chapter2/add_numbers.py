from linked_list import *

def add_numbers(num1, num2):
    carryover = 0
    result = Node(0)
    while num1 is not None or num2 is not None:
        if num1 is None:
            val1 = 0
        else:
            val1 = num1.value
            num1 = num1.next

        if num2 is None:
            val1 = 0
        else:
            val2 = num2.value
            num2 = num2.next

        total = val1 + val2 + carryover
        digit = total % 10 
        result.append(digit)
        carryover = total // 10
    return result.next
