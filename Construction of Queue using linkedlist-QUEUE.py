class node:
    def __init__(self,d):
        self.data = d 
        self.next = None

def printqueue(head):
    while head!=None:
        print(head.data , end=" ") 
        head = head.next 

def insert_at_end(head,element):
    temp = head  
    new_node = node(element) 
    if temp == None:
        return new_node
    while temp.next!=None:
        temp = temp.next 
    temp.next = new_node 
    return head 
def delete_at_start(head): 
    if head == None or head.next ==None:
        return None
    temp = head.next 
    return temp  
head = None 
lis = [10,20,30,40,50] 
for ele in lis:
    head = insert_at_end(head,ele) 
printqueue(head)   
print()
head = insert_at_end(head,60) 
printqueue(head) 
print()
head = delete_at_start(head) 
printqueue(head) 
print() 
