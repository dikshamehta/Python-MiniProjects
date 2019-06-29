avengers=("Tony Stark","Steve Rogers","Bruce Banner")
avengers1=("Nat","Thor","Clint")
print(avengers)
print(avengers[0])
print(avengers[0:3])

# avengers[0]='Nat' (This command does not work as tuple is immutable, it will give sytax error)

a,b,c= avengers
print(a)

print(len(avengers))

print(max(avengers))
print(min(avengers))

Theavengers= avengers+avengers1
print(Theavengers)
