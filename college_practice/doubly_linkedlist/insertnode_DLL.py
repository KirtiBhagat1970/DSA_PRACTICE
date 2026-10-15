class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert_node(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        temp = self.head

        # Insert at the first position
        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        # Find the node before the insertion position
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        # Update the next and previous pointers
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def print(self):
        temp = self.head
        print("List elements:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Create a doubly linked list
list = linkedlist()

# Append nodes
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

# Insert 90 at position 2
list.insert_node(Node(90), 2)

# Display the list
list.print()