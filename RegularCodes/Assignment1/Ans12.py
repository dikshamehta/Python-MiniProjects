'''Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My shown back to me. '''
str1=input("enter a long string")
str1=str1.split(" ")
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end=" ")
