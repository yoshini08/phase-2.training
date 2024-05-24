class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def print_linked_list(curr):
    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next
    print()
    
def insert_at_end(head, data):
    new_node = Node(data)  
    if head == None:
        return new_node
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return head

def delete_at_start(head):
    if head == None:
        return None
    return head.next

n = int(input())
head = None
data = list(map(int, input().split()))

for i in data:
    head = insert_at_end(head, i)
print_linked_list(head)

head = delete_at_start(head)
print_linked_list(head)
