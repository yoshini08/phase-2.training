def Enque(Q,ele):
    Q.append(ele)

def Deque(Q):
    if len(Q)==0:
        print("Queue is Empty")
        return
    Q.pop(0)

Q=[]
Enque(Q,2)
Enque(Q,3)
Enque(Q,4)
print(Q)
Deque(Q)
print(Q)
Deque(Q)
print(Q)
Deque(Q)
print(Q)
Deque(Q)
print(Q)

