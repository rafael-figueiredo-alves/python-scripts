# lists can be used as stacks in Python

stack = []

# push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)

# pop elements from the stack
top_element = stack.pop()
print("Popped element:", top_element)
print("Stack after pop:", stack)

# peek at the top element without removing it
top_element = stack[-1]
print("Top element (peek):", top_element)
print("Final stack state:", stack)

# check if the stack is empty
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)
# outro jeito de saber se a pilha está vazia
is_empty_alternate = not bool(stack)
print("Is the stack empty? (alternate method):", is_empty_alternate)

# get the size of the stack
stack_size = len(stack)
print("Current stack size:", stack_size)

# clear the stack
stack.clear()
print("Stack after clear:", stack)

# check if the stack is empty after clearing
is_empty_after_clear = len(stack) == 0
print("Is the stack empty after clear?", is_empty_after_clear)

# push more elements to demonstrate LIFO behavior
stack.append(4)
stack.append(5)
print("Stack after pushing 4 and 5:", stack)
popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after popping an element:", stack)

# definindo uma classe Stack para encapsular o comportamento de pilha

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

# Demonstrando o uso da classe Stack
stack_instance = Stack()
stack_instance.push(10)
stack_instance.push(20)
print("Stack instance after pushes:", stack_instance.items)
popped_from_instance = stack_instance.pop()
print("Popped from stack instance:", popped_from_instance)
print("Stack instance after pop:", stack_instance.items)
top_of_instance = stack_instance.peek()
print("Top of stack instance (peek):", top_of_instance)
print("Final stack instance state:", stack_instance.items)
print("Is stack instance empty?", stack_instance.is_empty())
print("Stack instance size:", stack_instance.size())
