'''Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates Given:
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Expected Outcome: [47, 52, 44, 53, 54] '''

dict={}
list=[]
while True:
    print("enter key nd value of dict nd pree q to exit")
    key=input()
    if(key=="q"):
        break
    value=input()
    dict[key]=value

for k,v in dict.items():
    if(list.count(v)==0):
        temp=v
        list.extend(temp)

print(list)
