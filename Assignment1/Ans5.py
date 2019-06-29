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
