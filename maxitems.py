from collections import Counter
def max_items(n):
    # s=Counter(n)
    s={}
    for i in n:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    max_item_help=max(s.keys())
    for i,j in s.items():
        if j==max((s.values())):
            if ord(max_item_help)>ord(i):
                max_item_help=i
                max_item=i
    return max_item


n=input()
print(max_items(n))