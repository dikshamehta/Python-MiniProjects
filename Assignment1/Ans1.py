list1=[]
n = int(input("Enter number of elements in list1 : "))
for i in range(0, n):
    e = int(input())
    list1.append(e)
list2 =[]
n = int(input("Enter number of elements in list2 : "))
for i in range(0, n):
    e = int(input())
    list2.append(e)
list3=[]
for i in range(1,len(list1),2):
    list3.append(list1[i])

for i in range(0,len(list1),2):
    list3.append(list2[i])

print(list3)
