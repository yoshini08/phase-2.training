class node:
    def __init__(self,d):
        self.left = None 
        self.data = d 
        self.right = None  
def inorder_traversal(root):
    if root == None:
        return 
    inorder_traversal(root.left) 
    print(root.data,end=" ") 
    inorder_traversal(root.right)
    
def preorder_traverseal(root):
    if root == None:
        return 
    print(root.data,end=" ") 
    preorder_traversal(root.left) 
    preorder_traversal(root.right)
    
def postorder_traverseal(root):
    if root == None:
        return 
    postorder_traversal(root.left) 
    postorder_traversal(root.right)
    print(root.data,end=" ") 

# Creation of nodes
obj1 = node(-105)
obj2 = node(-1)
obj3 = node(82)
obj4 = node(28)
obj5 = node(-15) 
obj6 = node(-18)  
obj7 = node(22) 
obj8 = node(27) 
# linking nodes
obj1.left = obj2 
obj1.right = obj3 
obj2.right = obj4 
obj4.left = obj8 
obj3.left = obj5 
obj5.left = obj6 
obj5.right = obj7  
# Traversals
inorder_traverseal(obj1) 
preorder_traversal(obj1) 
postorder_traversal(obj1)
