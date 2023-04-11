
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
        if root:
             print(str(root.val)+"->",end="")
             inorder(root.left)
             inorder(root.right)   

def preorder(root):
        if root:
            preorder(root.left)
            print(str(root.val)+"->",end="")
            preorder(root.right)   

def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(str(root.val)+"->",end="")
   

root=Node("A")

#left of root
root.left = Node("B")
root.left.left = Node("C")   
root.left.right = Node("D")
root.left.right.left = Node("H")

#right of root
root.right = Node("F")
root.right.left = Node("E")
root.right.left.right = Node("I")
root.right.right = Node("G")


print("Inorder transversal", inorder(root))
print("preorder traversal", preorder(root))
print("postorder traversal", postorder(root))




