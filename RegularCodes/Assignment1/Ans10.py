'''Print the following pattern
1
2 3 4
5 6 7 8 9
 '''
n= int(input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,(2*i)-1):
        print("j", end=" ")
    print("i")
