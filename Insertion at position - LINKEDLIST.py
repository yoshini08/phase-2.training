class node:
    def __init__(self,d):
        self.data = d 
        self.next = None   
def printlinkedlist(head): 
    while head!=None:
        print(head.data,end="-->") 
        head = head.next 
def insertion_at_end(head,element):
    new_node = node(element) 
    if head == None:
        return new_node 
    temp = head 
    while temp.next!= None:
        temp = temp.next 
    temp.next = new_node 
    return head 
def insertion_at_start(head,element): 
    new_node = node(element)
    if head == None: 
        return new_node 
    new_node.next = head 
    return new_node 
def insertion_at_position(head,pos,element):
    temp = head  
    new_node = node(element)  
    if pos==0:
        new_node.next = head 
        head.next = None 
        return new_node
    for i in range(pos-1):
        temp = temp.next  
    new_node.next = temp.next 
    temp.next = new_node 
    return head
head = None  
lis = [10,20,30,40,50]  
#INSERTION AT END
for element in lis:
    head  = insertion_at_end(head,element)    
# INSERTION AT START
head = insertion_at_start(head,element)  
# INSERTION AT POSITION 
head = insertion_at_position(head,3,100)
#printing linkedlist
printlinkedlist(head)   
print()
