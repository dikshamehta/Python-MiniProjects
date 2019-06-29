print("enter number of calls")
call_no= int(input())
cost=0;
if(call_no<=100 and call_no>=1):
    cost=cost+(1*call_no)
elif(call_no<=200 and call_no>=101):
    cost=cost+100+(0.5*call_no)
elif(call_no<=300 and call_no>=201):
    cost= cost + 200 + (0.25*call_no)
elif(call_no>=301):
    cost = cost + 300+ (0.10*call_no)
else:
    print("enter valid number")
GST_COST= (cost*18)/100;
print(GST_COST+cost)
