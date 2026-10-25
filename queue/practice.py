class Node:
    def __init__(self,value): # node initialize
        self.value=value # node first block 
        self.next=None  # points to next node

class Queue: 
    def __init__(self): # create empty queue
        self.front=self.rear=None # initialize queue as empty
    
    def enqueue(self,newnode):
        if self.rear: # if the rear exists is in the queue
            self.rear.next=newnode # rear next block points to newnode
            self.rear=newnode # rear is at position newnode
            
        else: # else block execute if queue is empty front=rear=None
            self.front=self.rear=newnode
    
    def dequeue(self):
        temp=self.front
        print(temp.value)
        self.front=self.front.next
        if self.front==None:
            print("queue is empty")
            self.rear=None
        temp=None
    def print(self):
        temp=self.front 
        while temp:
            print(temp.value)
            temp=temp.next
            
q=Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.enqueue(Node(50))
q.print()
q.dequeue()
q.print()

