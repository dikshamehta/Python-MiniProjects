import re
'''print("enter the student id")
id=input()
pattern=re.compile("\d{2}$")
check= pattern.match(id)
print(check)
if check==None:
    print("invalid input")


print("enter mobile number")
id=input()
pattern=re.compile("\d{10}$")
check= pattern.match(id)
print(check)
if check==None:
    print("invalid input")
exit()
\d{00,99}[(-F-)][(cs-)|(EC-)|(BT-)]
-1011-

phone_check = re.compile("[^0-9s-()]")

phone = input ("Please, enter your phone: ")

while phone_check.search(phone):
    print("Please enter your phone correctly!")
    phone = input ("Please, enter your phone: ")


'''
print("enter the student id")
id=input()
pattern=re.compile("^[U]\-\d{4}\-\d{00,99}\-[F]\-[(cs)|(ec)|(bt)]\-$")
check= pattern.match(id)
#print(check)
if check==None:
    print("invalid input")
