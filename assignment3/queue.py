class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self, value):
        newnode = Node(value)

        if self.isempty():
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Deleted element:", self.front.value)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 3. Display
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue elements:")

            while temp:
                print(temp.value)
                temp = temp.next

    # 4. Reverse Queue using Stack
    def reverse_queue(self):
        stack = []

        temp = self.front

        while temp:
            stack.append(temp.value)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(stack.pop())

        print("Queue reversed successfully")

    # 5. Merge Two Queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(temp.value)
            temp = temp.next

        print("Queues merged successfully")

    # 6. Check Identical Queues
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.value != temp2.value:
                print("Queues are not identical")
                return

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")


# Main Program

q1 = Queue()

q1.enqueue(99)
q1.enqueue(23)
q1.enqueue(47)

q1.display()

q1.dequeue()

q1.display()

q1.reverse_queue()

q1.display()


q2 = Queue()

q2.enqueue(10)
q2.enqueue(66)

q1.merge(q2)

q1.display()


q3 = Queue()

q3.enqueue(56)
q3.enqueue(40)
q3.enqueue(25)

q1.identical(q3)