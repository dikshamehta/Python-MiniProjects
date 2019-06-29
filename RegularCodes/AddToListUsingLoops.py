books=[]
while True:
    print("enter the name of the book")
    name= input()
    if(name=="q"):
        break

    books = books + [name]

print("Name of books in list")
for bname in range(len(books)):
    print(books[bname])
    #rolling dice 1) match the sum of dice with what user add , 5 attempts and correct him if he is not entering from 2 to 12
