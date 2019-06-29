num= int(input("enter a number"))
print("divisors are:" )
for i in range(1,int((num/2))+1):
    if((num%i)==0):
        print(str(i)+" ",end=" ")
print(num,end=" ")
