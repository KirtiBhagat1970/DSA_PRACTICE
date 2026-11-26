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
    
    def inorder(self,temp): #recursive call
        if temp is None: # terminating condition of inorder
            return
        else:
            self.inorder(temp.left)    
            print(temp.value,end=" ")
            self.inorder(temp.right)      
    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
            return
        
        arr=[]
        cnt=0  #for counting visited node
        level=0
        arr.append(rt)
        while cnt < len(arr):
            node_count=len(arr)-cnt  #number of nodes to be visited
            print(f"\nLevel {level} nodes:",end=" ")
            for i in range(node_count):
                temp=arr[cnt]
                cnt+=1
                print(temp.value,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1
        print("\nHeight of tree:",level-1)       
            
                           
b=BST() 
b.insert(Node(100))   
b.insert(Node(10)) 
b.insert(Node(450))   
b.insert(Node(4)) 
b.insert(Node(300))  
b.insert(Node(500)) 
b.insert(Node(50)) 
b.insert(Node(70))
b.insert(Node(2))  

print("Inorder traversal:")
b.inorder(b.root)
print("\nlevel order:")
b.level_order(b.root)
  
            
                