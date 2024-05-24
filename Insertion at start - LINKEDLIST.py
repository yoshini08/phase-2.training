class node:
    def __init__(self,d):
        self.data = d 
        self.next = None   
def printlinkedlist(head): 
    while head!=None:
        print(head.data,end="-->") 
        head = head.next 
def insertion_at_start(head,element): 
    new_node = node(element)
    if head == None: 
        return new_node 
    new_node.next = head 
    return new_node 
head = None  
lis = [10,20,30,40,50]  
#INSERTION AT END
for element in lis:
    head  = insertion_at_end(head,element)  
# INSERTION AT START
head = insertion_at_start(head,element) 
