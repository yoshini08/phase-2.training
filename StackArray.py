def push(Q,ele):
    Q.append(ele)

def pop(Q):
    if len(Q)==0:
        print("Queue is Empty")
        return
    Q.pop()

Q=[]
push(Q,2)
push(Q,3)
push(Q,4)
print(Q)
pop(Q)
print(Q)
pop(Q)
print(Q)
pop(Q)
print(Q)
pop(Q)
print(Q)