class Node:
    def __init__(self,value):
        self.left=None
        self.value=value
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
    
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
    
    def preorder(self,temp): #recursive call
        if temp is None: # terminating condition of inorder
            return
        else:
            print(temp.value,end=" ")
            self.preorder(temp.left)    
            self.preorder(temp.right)      
               
        
            
b=BST() 
b.insert(Node(10))   
b.insert(Node(5)) 
b.insert(Node(-2))   
b.insert(Node(25)) 
b.insert(Node(13))  
b.insert(Node(40)) 
b.preorder(b.root)