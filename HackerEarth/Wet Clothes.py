n, m, g = map(int,input().split())
time = list(map(int,input().split()))
arr = list(map(int,input().split()))
lst = []
c= 0
for i in range(0,n-1):
    x = time[i+1]-time[i]
    lst.append(x)
    
m = max(lst)
c=0
for i in range(len(arr)):
    if arr[i]<=m:
        c+=1
print(c)
