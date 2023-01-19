class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="-->")
            temp = temp.next
        print("None")

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.head.next is None:
            self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        self.head.next = new_node
        self.tail = new_node


link = LinkedList()
link.prepend(9)
link.prepend(5)
link.prepend(6)
link.append(4)
# print(link.head.value)
link.print_list( )
