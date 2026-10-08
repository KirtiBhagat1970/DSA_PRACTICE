class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
            
    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sum.")
            return
        
        temp=self.head
        while temp and temp.next:
            consecutive_sum=temp.data+temp.next.data
            print(f"sum of {temp.data} and {temp.next.data}={consecutive_sum}")
            temp=temp.next
            
list=LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.sum_consecutive()

        
        
            
        