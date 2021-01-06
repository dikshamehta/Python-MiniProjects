'''Write a Python program to create the multiplication table (from 1 to 10) of a number. '''

print("Enter the number")
n=int(input())
for i in range(1,11):
    r= n*i
    print(str(n)+" * "+str(i)+" = "+str(r))
