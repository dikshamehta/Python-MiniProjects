'''We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2. characters position doesn’t matter.
For Example: –
S1=yn
S2=Pynative
Output=True '''

s1= input("enter string 1")
s2= input("enter string 2")

print(s2 in s1)
