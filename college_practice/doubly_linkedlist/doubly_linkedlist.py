class Node:
    def __init(self,value):
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
            
list=linkedlist()         
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)

list.append(Node(10))
list.append(Node(20))
# li.append(n3)
# li.append(n4)
list.print()