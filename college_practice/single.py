class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
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
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
n1=Node(20)
n2=Node(30)
list=Linkedlist()
list.append(n1)
list.append(n2)
list.print()



        
                