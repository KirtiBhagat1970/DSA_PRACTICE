# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right
    def del_node(self,rt,value):
        if rt is None:
            return rt
        if value < rt.data:
            rt.left = self.del_node(rt.left,value)
        elif value > rt.data:
            rt.right = self.del_node(rt.right,value)
        else:
            if rt.left is None: # Node with right child only
                return rt.right
            if rt.right is None: # Node with left child only
                return rt.left          
            # Node has both left and right children
            succ = self.get_sucessor(rt)
            rt.data = succ.data
            rt.right=self.del_node(rt.right,succ.data)  
        return rt
    def get_successor(self,temp):
        temp = temp.right
        while temp.left is not None :
            temp = temp.left
        return temp
    def search(self,key):
        temp = self.root
        while temp:
            if temp.data==key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    # Inorder traversal (Left, Root, Right)
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Count total nodes
    def count_nodes(self, rt):
        if rt is None:
            return 0
        return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    # Count leaf nodes
    def count_leaf(self, rt):
        if rt is None:
            return 0
        if rt.left is None and rt.right is None:
            return 1
        return self.count_leaf(rt.left) + self.count_leaf(rt.right)

    # Count non-leaf nodes
    def count_nonleaf(self, rt):
        if rt is None:
            return 0
        if rt.left is None and rt.right is None:
            return 0
        return 1 + self.count_nonleaf(rt.left) + self.count_nonleaf(rt.right)

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right

        print("Max:", temp.data)


# Main program

b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(300))
b1.insert(Node(50))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(70))
b1.insert(Node(2))

print("\nInorder:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

print("\nTotal nodes:", b1.count_nodes(b1.root))
print("Leaf nodes:", b1.count_leaf(b1.root))
print("Non-leaf nodes:", b1.count_nonleaf(b1.root))

b1.findminmax()

#b1.del_node(b1.root,2)
#print("\nAfter Deletion:",end =" ")
#b1.inorder(b1.root)

b1.del_node(b1.root,4)
print("\nAfter Deletion:",end =" ")
b1.inorder(b1.root)

if b1.search(450):
    print("\nFound the node")
else:
    print("\nNot found")