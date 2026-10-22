class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def isempty(self):
        return self.top is None
    def push(self,newnode):
        newnode.next=self.top 
        self.top=newnode # top points to newnode
    
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("popped element:",temp.value)
            self.top=self.top.next
            temp=None
    def print(self):
        if self.isempty():
            print("stack is empty")
        
        else:
            print("stack contains:")
            temp=self.top
            while temp:
                print(temp.value)
                temp=temp.next
            
s=Stack()

s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.print()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.print()
