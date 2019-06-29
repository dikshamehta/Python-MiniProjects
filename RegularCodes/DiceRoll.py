import random
min=1
max=6
attempt=1

while attempt<=6:
    d1= random.randint(min,max)
    d2= random.randint(min,max)
    sum= d1+d2
    print("attempt no."+str(attempt))
    print("Guess the sum")
    guess=int(input())
    if(guess==sum):
        print("Hurray!! you have got it")
        break
    elif(guess>12 or guess<2):
        print("please enter within valid range i.e from 2 to 12")
    else:
        print("nahh!! please try again")
    attempt=attempt+1
