avengers=["Tony Stark","Steve Rogers","Bruce Banner"]
avengers1=["Nat","Thor","Clint"]
random=["b","a","a","b"]
print(random.count("b"))
print(avengers)
print(avengers1)

avengers[0]='Anthony Edward Stark'
print(avengers,avengers1)
avengers1
a,b,c=avengers
print(a)

print(avengers[0:3:2])

del random[0]
print(random)

print(max(avengers))

print(sorted(avengers))
print(avengers)

avengers.sort()
print(avengers)

avengers.append("Stephen Strange")
print(avengers)

avengers.extend(avengers1)
print(avengers)
