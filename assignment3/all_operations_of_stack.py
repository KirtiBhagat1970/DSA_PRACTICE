class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push operation
    def push(self, value):
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode

    # 2. Pop operation
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.value)
            self.top = self.top.next

    # 3. Display operation
    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp:
                print(temp.value)
                temp = temp.next

    # 4. Reverse String using Stack
    
    def reverse_string(self, string):
        s2 = Stack()
        for ch in string:
            s2.push(ch)

        result = ""

        while not s2.isempty():
            result += s2.top.value
            s2.top = s2.top.next

        print("Reversed String:", result)

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        s2 = Stack()

        while not self.isempty():
            value = self.top.value
            self.top = self.top.next
            s2.push(value)

        self.top = s2.top

        print("Stack reversed successfully")


# Main Program
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

s.pop()

s.display()

s.reverse_string("PYTHON")

s.reverse_stack()

s.display()