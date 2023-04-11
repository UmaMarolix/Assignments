#Creating Binary tree
#Class that represents an individual node of the binary tree
class Node:
    
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

# traversal method inorder--left,root right
def tInorder(root):
    if root:
        tInorder(root.left)
        print(root.val)
        tInorder(root.right)

#traversal method postoreder--left,right,root
def tpostorder(root):
        if root:
            tpostorder(root.left)
            tpostorder(root.right)
            print(root.val)

#traversal method pretoreder--root,left,right
def tpreorder(root):
        if root:
            print(root.val)
            tpreorder(root.left)
            tpostorder(root.right)


#creating a root
root=Node(10)

        
root.left=Node(33)
root.right=Node(45)


  
root.left.left=Node(11)
root.left.right=Node(20)

root.right.left=Node(33)

print("preorder traversal of binary tree is:", tpreorder(root))
print("Inorder traversal of binary tree is:", tInorder(root))
print("postorder traversal of binary tree is:", tpostorder(root))
