arr = [10,20,30,50,100] 
target = 100 
pos = -1 
left,right = 0 ,len(arr)-1 
while left<=right: 
  mid = (left + right)//2 
  if arr[mid]<target:
    left = mid+1 
  elif arr[mid]>target:
    right = mid-1 
  elif arr[mid] == target:
    pos = mid 
if pos==-1:
  print("Element not found") 
else:
  print("Element found",pos)
