class node:
    def __init__(self,d):
        self.data = d 
        self.next = None 
def printLinkedList(head): 
    while head!=None: 
        print(head.data, end=" ")
        head = head.next  
def insert(head,new_node): 
    linked_node = node(new_node) 
    if head == None:
        return linked_node 
    temp = head 
    while temp.next!= None: 
        temp = temp.next  
    temp.next = linked_node 
    return head 
head = None
n = int(input())  
lis = map(int,input().split())
for i in lis: 
    head = insert(head,i)  
printLinkedList(head)
    
    
