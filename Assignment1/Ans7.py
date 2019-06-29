l1=[]
d={}
print("enter the number of element to enter")
n=int(input())

for i in range(0,n):
    e=int(input())
    l1.append(e)

for i in l1:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1

print(d)
