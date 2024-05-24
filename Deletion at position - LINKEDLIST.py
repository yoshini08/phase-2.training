class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def print_linked_list(curr):
    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next
    print()
    
def insert_at_begin(head,data):
    new_node = node(data)
    if head == None:
        return new_node
    return head.next
    
    
def insert_at_end(head, data):
    new_node = Node(data)  
    if head == None:
        return new_node
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return head
def delete_at_position(head,pos):
    if head == None:
        return None
    if pos == 0:
        return head.next
    currindex = 1
    currnode = head
    while currindex != pos-1:
        currindex +=1
        currnode = currnode.next
    temp= currnode.next
    currnode.next = temp.next
    temp.next = None

    return head
        
    
n = int(input())
head = None
data = list(map(int, input().split()))
pos=int(input())

for i in data:
    head = insert_at_end(head, i)
print_linked_list(head)

head = delete_at_position(head,pos)
print_linked_list(head)
