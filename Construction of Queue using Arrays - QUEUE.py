queue = []  
#insertion at end
def insert(element):
    queue.append(element)  
    return queue  
#deletion at start
def remove():  
    if not queue:
        print("Queue is empty")
    print(queue.pop(0))  
#top element
def print_top(): 
    if not queue:
        print("Queue is empty")
    print(queue[0]) 
#print queue
def printqueue():
    if not queue:
        print("Queue is empty")
    for i in queue:
        print(i,end=" ") 
    print()  
# length of queue
def checklength(): 
    if queue:
        print("Queue is not empty") 
    else:
        print("Queue is empty") 
head = None
n = int(input())
for _ in range(n):
    user = list(map(int, input().split()))
    if user[0] == 1:
        insert(user[1])
        print(user[1], "inserted")
    elif user[0] == 2:
        print_top()
    elif user[0] == 3:
        head = remove()
    elif user[0] == 4:
        printqueue()
    elif user[0] == 5:
        checklength()
    
