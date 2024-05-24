class Box:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printpreordertraversal(root):
    if root == None:
        return
    print(root.data,end = " ") 
    printpreordertraversal(root.left)
    printpreordertraversal(root.right)       
obj1 = Box(-105) 
obj2 = Box(1)    
obj3 = Box(28)    
obj4 = Box(27)    
obj5 = Box(82)
obj6 = Box(-15)
obj7 = Box(-18)
obj8 = Box(22) 

obj1.left=obj2 
obj2.right=obj3
obj3.left=obj4
obj1.right=obj5
obj5.left=obj6
obj6.left=obj7
obj6.right=obj8

printpreordertraversal(obj1)
