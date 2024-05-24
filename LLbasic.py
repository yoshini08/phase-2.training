class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def PrintLL(head):
    while head:
        print(head.data,end="->")
        head=head.next
    print(None)

def InsertAtLast(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next:
        tail=tail.next
    tail.next=temp
    return head

def InsertAtBegin(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    temp.next=head
    return temp

def InsertAtParticularPos(head,ele,pos):
    temp=Node(ele)
    c=0
    tail=head
    while tail.next:
        c+=1
        if c==pos:
            temp.next=tail.next
            tail.next=temp
        tail=tail.next
    return head

def DeleteAtLast(head):
    tail=head
    if tail==None or tail.next==None:
        return None
    
    while tail.next.next:
        tail=tail.next
    tail.next=None
    return head

def DeleteAtBegin(head):
    if head==None or head.next==None:
        return None
    head=head.next
    return head

def DeleteAtParticularPos(head,pos):
    if pos==0:
        return DeleteAtBegin(head)
    c=0
    tail=head
    while c!=pos-1:
        c+=1
        tail=tail.next
    temp=tail.next
    tail.next=temp.next
    return head

l=[1,2,3,4,5,6,7,8,9,10]
head=None
for i in l:
    head=InsertAtLast(head,i)
PrintLL(head)
head=InsertAtBegin(head,69)
PrintLL(head)
head=InsertAtParticularPos(head,6969,3)
PrintLL(head)
head=DeleteAtLast(head)
PrintLL(head)
head=DeleteAtBegin(head)
PrintLL(head)
head=DeleteAtParticularPos(head,2)
PrintLL(head)