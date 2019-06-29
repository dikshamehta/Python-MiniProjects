l1=[]
l2=[]
l3=[]

n = int(input("Enter number of elements in list1 : "))
for i in range(0, n):
    e = int(input())
    if(l1.count(e)==0):
        l1.append(e)

n1 = int(input("Enter number of elements in list2 : "))
for i in range(0, n1):
    e = int(input())
    if(l2.count(e)==0):
        l2.append(e)

l1.extend(l2)

for i in range(0,len(l1)):
    if(l3.count(l1[i])==0):
        l3.append(l1[i])

print(l3)
