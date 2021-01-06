'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game) Remember the rules:
    • Rock beats scissors
    • Scissors beats paper
    • Paper beats rock 
'''
p1=input("player 1 please enter r for rock, p for paper, s for Scissors")
p2=input("player 2 please enter r for rock, p for paper, s for Scissors")

if(p1=="r" and p2=="s"):
    print("player 1 wins")
elif(p1=="r" and p2=="p"):
    print("player 2 wins")
elif(p1=="s" and p2=="p"):
    print("player 1 wins")
elif(p1=="s" and p2=="r"):
    print("player 2 wins")
elif(p1=="p" and p2=="s"):
    print("player 2 wins")
elif(p1=="p" and p2=="r"):
    print("player 1 wins")
else:
    print("tie")
