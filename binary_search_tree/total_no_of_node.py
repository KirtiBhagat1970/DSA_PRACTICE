class Node:
    def __init__(self,value):  #create node
        self.left=None
        self.value=value
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
        self.count=0
    
    def insert(self,newnode):
        if self.root is None: #creating the root node
            self.root=newnode
            return
        else:
            temp=self.root 
            while True:
                if newnode.value < temp.value:  #left subtree
                    if temp.left is None:
                        temp.left=newnode
                        return
                    else:
                        temp=temp.left
                elif newnode.value >= temp.value:
                    if temp.right is None: # right subtree
                        temp.right=newnode
                        return
                    else:
                        temp=temp.right
    
    def inorder(self,temp): #recursive call
        if temp is None: # terminating condition of inorder
            return
        else:
            self.inorder(temp.left)    
            print(temp.value,end=" ")
            self.count+=1             #count total numbers of node
            self.inorder(temp.right)      
    
    def preorder(self,temp): #recursive call
            if temp is None: # terminating condition of inorder
                return
            else:
                print(temp.value,end=" ")
                self.count+=1             #count total numbers of node
                self.preorder(temp.left)    
                self.preorder(temp.right)            
    def postorder(self,temp): #recursive call
            if temp is None: # terminating condition of inorder
                return
            else:
                self.postorder(temp.left)    
                self.postorder(temp.right) 
                print(temp.value,end=" ")   #count total numbers of node
                self.count+=1   
                       
            
b=BST() 
b.insert(Node(100))   
b.insert(Node(10)) 
b.insert(Node(450))   
b.insert(Node(4)) 
b.insert(Node(65))  
b.insert(Node(300)) 
b.insert(Node(500)) 
b.insert(Node(50)) 
b.inorder(b.root)
print("\n Total nodes:",b.count) #call varibale to display count of nodes
b.preorder(b.root)
b.postorder(b.root)
  
            
                