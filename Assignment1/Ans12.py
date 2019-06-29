str1=input("enter a long string")
str1=str1.split(" ")
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end=" ")
