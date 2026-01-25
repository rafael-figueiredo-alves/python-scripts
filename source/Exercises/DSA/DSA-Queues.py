# A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

"""
Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket.

Basic operations we can do on a queue are:

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Queues are often mentioned together with Stacks, which is a similar data structure described on the previous page.
"""

queue = []

# enqueue elements to the queue
queue.append("John")
queue.append("Mary")
queue.append("Steve")
print("Queue after enqueues:", queue)
queue.append("Anna")
print("Queue after enqueueing Anna:", queue)

# dequeue elements from the queue
queued_element = queue.pop(0)
print("Dequeued element:", queued_element)
print("Queue after dequeue:", queue)
queue.pop(0)
print("Queue after another dequeue:", queue)

# peek at the front element without removing it
front_element = queue[0]
print("Front element (peek):", front_element)
print("Final queue state:", queue)

# check if the queue is empty
is_empty = len(queue) == 0
isEmpty = not bool(queue)
print("Is the queue empty?", is_empty)
print("Is the queue empty? (alternate method):", isEmpty)

# get the size of the queue
queue_size = len(queue)
print("Current queue size:", queue_size)

# clear the queue
queue.clear()
print("Queue after clear:", queue)

# Note: While using a list is simple, removing elements from the beginning (dequeue operation) requires shifting all remaining elements, making it less efficient for large queues.

# definindo uma classe Queue para encapsular o comportamento de fila

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
    
# exemplo de uso da classe Queue
queue = Queue()
queue.enqueue("John")
queue.enqueue("Mary")
print("Queue after enqueues:", queue.items)
dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", queue.items)
print("Front element (peek):", queue.peek())
print("Is the queue empty?", queue.is_empty())
print("Current queue size:", queue.size())
# outro jeito de saber se a fila está vazia
print("Is the queue empty? (alternate method):", not bool(queue.items))
queue.clear()
print("Queue after clear:", queue.items)

# Implementando Queue usando collections.deque para melhor desempenho

from collections import deque

class DequeQueue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
    

# exemplo de uso da classe DequeQueue
deque_queue = DequeQueue()
deque_queue.enqueue("John")
deque_queue.enqueue("Mary")
print("DequeQueue after enqueues:", deque_queue.items)
dequeued_element = deque_queue.dequeue()
print("Dequeued element from DequeQueue:", dequeued_element)
print("DequeQueue after dequeue:", deque_queue.items)
print("Front element (peek) from DequeQueue:", deque_queue.peek())
print("Is the DequeQueue empty?", deque_queue.is_empty())
print("Current DequeQueue size:", deque_queue.size())
# outro jeito de saber se a DequeQueue está vazia
print("Is the DequeQueue empty? (alternate method):", not bool(deque_queue.items))
deque_queue.clear()
print("DequeQueue after clear:", deque_queue.items)

# Note: Using collections.deque is more efficient for queue operations as it allows O(1) time complexity for both enqueue and dequeue operations.

# implementando queue com linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0

# exemplo de uso da classe LinkedListQueue
linked_list_queue = LinkedListQueue()
linked_list_queue.enqueue("John")
linked_list_queue.enqueue("Mary")
linked_list_queue.enqueue("Steve")
linked_list_queue.enqueue("Anna")
linked_list_queue.enqueue("Bob")
print("LinkedListQueue after enqueues:", [linked_list_queue.peek()] + ["..."] * (linked_list_queue.get_size() - 1))        
dequeued_element = linked_list_queue.dequeue()
print("Dequeued element from LinkedListQueue:", dequeued_element)
print("LinkedListQueue after dequeue:", [linked_list_queue.peek()] + ["..."] * (linked_list_queue.get_size() - 1) if not linked_list_queue.is_empty() else [])
print("Front element (peek) from LinkedListQueue:", linked_list_queue.peek())
print("Is the LinkedListQueue empty?", linked_list_queue.is_empty())
print("Current LinkedListQueue size:", linked_list_queue.get_size())
print("Is the LinkedListQueue empty? (alternate method):", not bool(linked_list_queue.get_size()))
linked_list_queue.clear()
print("LinkedListQueue after clear:", linked_list_queue.get_size())