class Node:
    def __init__(self,val):
        self.data=val  # store the value in node
        self.next=None # next node address is none

#create linked list
class Linkedlist:
    def __init__(self):
        self.head=None # initially linked list is empty

    def append(self,new_node):
        if self.head==None: # check if linked list is empty
            self.head=new_node # make new node as head
        else:
            temp=self.head # start from head
            while temp.next: # traverse till last node
                temp=temp.next # move to next node
            temp.next=new_node # add new node at the end
            
    # 2.traverse and print the node values
    def print(self):
        temp=self.head #start from head
        while temp: #traverse till last node
            print(temp.data) #move to next node
            temp=temp.next #add new node at the end
    
    def display(self):
        temp = self.head  # start from head

        while temp:
            print(temp.data, end=" -> ")  # print node value
            temp = temp.next  # move to next node
        print("None")
    
    #3. insert node at a specific position        
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
    
    #4.find middle node and print its value   
    def middle_node(self):
        if self.head == None:
           print("Linked list is empty")
           return

        slow = self.head  # move one node at a time
        fast = self.head  # move two nodes at a time

        while fast != None and fast.next != None:
           slow = slow.next  # move one step
           fast = fast.next.next  # move two steps

        print("Middle node:", slow.data)  # print middle node value
        
    # 5.delete node
    def del_node(self, value):
        temp = self.head
        prev = None

    # check if linked list is empty
        if temp == None:
           print("Linked list is empty")
           return

    # deleting first node
        if temp.data == value:
           self.head = self.head.next
           return

        while temp:
            if temp.data == value:  # searching value
               break
            else:
                prev = temp  # store previous node
                temp = temp.next  # traverse to next node

        if temp == None:  # check if value is present
            print("Value is not present in list")
            return

        prev.next = temp.next  # connect previous node to next node
        temp = None  # delete node reference
        
    #6.reverse a list
    def reverse_node(self):
        curr = self.head  # start from head
        prev = None       # previous node is none

        while curr:
            nextnode = curr.next  # store next node
            curr.next = prev      # reverse the link
            prev = curr            # move prev to current node
            curr = nextnode        # move curr to next node
        self.head = prev  # update head to new first node
        
    #7.calculate the sum of every two consecutive node values
    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sum.")
            return

        temp = self.head  # start from head

        while temp and temp.next:
            consecutive_sum = temp.data + temp.next.data  # add consecutive nodes
            print(f"sum of {temp.data} and {temp.next.data}={consecutive_sum}")
            temp = temp.next  # move to next node
        
        
# create object
ll = Linkedlist()

# add nodes
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))
ll.append(Node(50))

# insert node
ll.insert_node(2, 15)

# find middle node
ll.middle_node()

# delete node
ll.del_node(30)

# reverse linked list
ll.reverse_node()

# sum of consecutive nodes
ll.sum_consecutive()

ll.display()

