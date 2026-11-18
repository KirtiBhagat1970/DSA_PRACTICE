
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, newnode):
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            temp = self.top
            popped_data = temp.value
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.value)
                temp = temp.next


class Lqueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        deleted_data = temp.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        temp = None
        return deleted_data

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


# Reverse stack using queue
def reverse_stack(s1):
    q1 = Lqueue()

    while not s1.isempty():
        data = s1.pop()
        q1.enqueue(Node(data))

    print("Queue after transferring stack elements:")
    q1.print()

    return q1


s = Stack()

s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))

s.print()

q = reverse_stack(s)
