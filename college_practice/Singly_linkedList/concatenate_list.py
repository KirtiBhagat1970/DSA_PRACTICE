class Node:
    def __init__(self,data):
        self.data=data
        self.head=None
class LinkedList:
    def __init__(self):
            self.head=None #initialize linked list is empty
    def append(self,new_node):
        if self.head==None: #check if linked list is empty
            self.head=new_node #make new node as head
        else:
            temp=self.head #start from head
            while temp.next: #traverse till last node
                temp=temp.next #move to next node
            temp.next=new_node #add new node as head
                
       
        # 2.traverse and print the node values
    def print(self):
        temp=self.head #start from head
        while temp: #traverse till last node
            print(temp.data) #move to next node
            temp=temp.next #add new node at the end
            
    def concatenate(self,other_list):
        if self.head==None:
            self.head=other_list.head
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=other_list.head
                
list=LinkedList()
list2=LinkedList()
list2.append(Node(50))
list2.append(Node(60))
list2.append(Node(70))

n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.concatenate(list2)
list.print()
            
            
    
            
        