import random
min=1
max=20
random_no= random.randint(min,max)
print(random_no)
attempt_no=1
while attempt_no!=7:
    print("Enter the number")
    guess=int(input())
    if(guess==random_no):
        print("correct answer in attempt no : "+str(attempt_no))
        break
    elif(guess<random_no):
        print("too low")
    elif(guess>random_no):
        print("too high")
    attempt_no=attempt_no+1
    print("moving towards "+str(attempt_no)+"  attempt")
