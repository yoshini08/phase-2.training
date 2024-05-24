class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def PrintLL(head):
    while head:
        print(head.data,end="->")
        head=head.next
    print(None)

def Enque(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next:
        tail=tail.next
    tail.next=temp
    return head

def Deque(head):
    if head==None or head.next==None:
        return None
    head=head.next
    return head

head=None
head=Enque(head,22)
head=Enque(head,33)
head=Enque(head,44)
head=Enque(head,55)
PrintLL(head)
head=Deque(head)
PrintLL(head)
head=Deque(head)
PrintLL(head)


