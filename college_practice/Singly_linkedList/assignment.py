class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
                
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next   
            
    
    def reverse_node(self):
        curr=self.head
        prev=None
        while (curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev
    
    def consecutive_sum(self):
        if not self.head and self.head.next:
            print("not enough nodes to calculate sum of consecutive")
            return
        
        temp=self.head
        while temp and temp.next:
            sum_consecutive=temp.data + temp.next.data
            print(f"sum of {temp.data} and {temp.next.data}={sum_consecutive}")
            temp=temp.next
            
    def insert_node(self, pos, data):
    if pos < 1:
        print("Invalid position")
        return

    new_node = Node(data)  # create new node

    if pos == 1:
        new_node.next = self.head  # connect new node to head
        self.head = new_node  # make new node as head
        return

    temp = self.head  # start from head
    curr_pos = 1  # current position

    while curr_pos < pos - 1 and temp != None:
        temp = temp.next  # move to next node
        curr_pos += 1  # increase current position

    if temp == None:
        print("Invalid position")
        return

    new_node.next = temp.next  # connect new node to next node
    temp.next = new_node  # insert new node at given position
        
    def delete_at_position(self, pos):
        if self.head == None:
            print("List is empty")
            return

        if pos <= 0:
            print("Invalid position")
            return

        # Delete first node
        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        # Reach the node before the position
        for i in range(1, pos - 1):
            if temp.next == None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next == None:
            print("Position out of range")
            return

        # Delete the node
        temp.next = temp.next.next   
            
    
               
        
                         
li=Linkedlist()
n1=Node(10)
n2=Node(20)
n3=Node(30)  
n4=Node(40)   
li.append(n1)
li.append(n2)
li.append(n3)
li.append(n4)
# li.print()  
# li.reverse_node() 
# li.print() 
# li.consecutive_sum()
# li.insert_node(60,3)
# li.print()
li.delete_at_position(3)
li.print()

