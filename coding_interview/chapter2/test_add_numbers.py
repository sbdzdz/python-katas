from linked_list import *
from add_numbers import *

def test_simple():
    num1 = [3, 1, 5]
    num2 = [5, 9, 2]
    result = add_numbers(list2linked(num1), list2linked(num2))
    assert linked2list(result) == [8, 0, 8]

def test_hard():
    num1 = 12039487201398472347878
    num2 = 82039013984722433347575
    total = list(int(i) for i in reversed(str(num1 + num2)))
    l1 = list(int(i) for i in reversed(str(num1)))
    l2 = list(int(i) for i in reversed(str(num2)))
    result = add_numbers(list2linked(l1), list2linked(l2))
    assert linked2list(result) == total 
