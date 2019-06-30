'''Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
For example: list = [10, 20, 30, 10, 20, 40, 50]
Expected Outcome: dict = {10: 2, 20: 2, 30: 1, 40: 1, 50: 1}'''

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
