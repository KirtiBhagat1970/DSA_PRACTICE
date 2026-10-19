class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:#first node
            self.head=new_node
    def print(self):
        temp=self.head
        print("List elements:")
        while temp:
            print(temp.data)
            temp=temp.next
    
        
    def swap_node(self):
        node1=self.head #node1 is  first node
        temp=self.head
        while temp.next: #temp is last node 
            temp=temp.next
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp
       
            
            
list=linkedlist()         
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

list.append(Node(10))
list.append(Node(20))
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.print()
list.swap_node()
list.print()