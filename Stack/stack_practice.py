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
        self.top=newnode
    
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("pop element:",temp.value)
            self.top=self.top.next
            temp=None
            
    def reverse(self):
        temp=self.top
        while temp:
            s1.push(Node(temp.value))
            temp=temp.next
        
    def print(self):
        temp=self.top
        while temp:
            print("stack element:",temp.value)
            temp=temp.next

s=Stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
# s.print()
s1=Stack()
s.reverse()
s1.print()
    
    