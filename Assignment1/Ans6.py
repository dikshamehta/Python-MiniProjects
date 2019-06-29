s1=input("enter the String: ")
s2=""
s3=""

for i in range(len(s1)):
    if(s1[i].islower()):
        s2=s2+s1[i]
    else:
        s3=s3+s1[i]
print(s2+s3)
