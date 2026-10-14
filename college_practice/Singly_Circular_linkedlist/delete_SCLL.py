class Node:
    def __init__(self,val):
        self.data=val #store value in node
        self.next=None #next node address is none
        
# 1.create linked list
class Cirular_Linkedlist:
    def __init__(self):
        self.head=None #initialize linked list is empty
        
    def append(self,new_node):
        if self.head==None: #check if linked list is empty
            self.head=new_node #make new node as head
            new_node.next=self.head
        else:
            temp=self.head #start from head
            while (temp.next!=self.head): #traverse till last node
                temp=temp.next #move to next node
            temp.next=new_node #add new node as head
            new_node.next=self.head
            
   #delete a specific node in singly circular linked list
    def del_node(self,value):
            temp=self.head
            prev=None
            #deleting first node
            
            if temp.data==value:
                while(temp.next !=self.head):
                    temp=temp.next
                self.head=self.head.next
                temp.next=self.head
        
            else:
                while(temp.data!=value):
                    prev=temp
                    temp=temp.next
                    if temp==self.head:
                        print("Value is not present in list")
                        return
                prev.next=temp.next
                temp=None  
                          
    # 2.traverse and print the node values
    def print(self):
        temp=self.head #start from head
        while True: #traverse till last node
            print(temp.data) #move to next node
            temp=temp.next #add new node at the end
            if temp==self.head:
                break
            
list=Cirular_Linkedlist()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.del_node(30)
list.print()
        
        

        