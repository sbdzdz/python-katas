from queue import *

classes = [Queue, NodeQueue, MyQueue]

def test_dequeue_empty():
    for Queue in classes:
        queue = Queue()
        assert queue.dequeue() is None

def test_enqueue_dequeue():
    for Queue in classes:
        queue = Queue()
        queue.enqueue(1)
        assert queue.dequeue() == 1
        assert queue.dequeue() is None 

def test_fifo():
    for Queue in classes:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() is None 
