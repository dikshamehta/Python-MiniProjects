anime= {}
while True:
    print("enter the name of anime and a character within it, also enter q to exit")
    name=input()

    if(name=="q"):
        break

    char=input()

    #anime2={name:char}
    #anime.update(anime2)
    anime[name]=char

for k,v in anime.items():
    print(k,v)
