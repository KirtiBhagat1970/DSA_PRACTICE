class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next=newnode
            self.rear=newnode
        else:
            self.front=self.rear=newnode
    def print(self):
        temp=self.front
        while temp:
            print(temp.value,end="->")
            temp=temp.next     
que=Lqueue()
que.enqueue(Node(23))
que.enqueue(Node(56))
que.enqueue(Node(67))
que.enqueue(Node(45))
que.print()