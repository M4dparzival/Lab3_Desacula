class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            return None
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data


ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.display()

print("Removed from beginning:", ll.remove_beginning())
print("Removed from end:", ll.remove_at_end())
print("Removed value 20:", ll.remove_at(20))
print("Removed value 99 (not found):", ll.remove_at(99))
ll.display()
