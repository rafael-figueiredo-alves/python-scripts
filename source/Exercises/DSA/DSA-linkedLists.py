# Linked Lists are linear data structures where elements, called nodes,
# are stored in a sequence.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("LinkedList contents:", elements)

# exemplo de uso da classe LinkedList
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.prepend(0)
linked_list.display()
linked_list.delete_with_value(2)
linked_list.display()
linked_list.delete_with_value(0)
linked_list.display()
linked_list.delete_with_value(3)  # tentando deletar um valor que não existe
linked_list.display()
linked_list.delete_with_value(1)
linked_list.display()
linked_list.append(5)
linked_list.display()
linked_list.prepend(10)
linked_list.display()