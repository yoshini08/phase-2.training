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
head = None  
lis = [10,20,30,40,50]  
#INSERTION AT END
for element in lis:
    head  = insertion_at_end(head,element)  
printlinkedlist(head)
