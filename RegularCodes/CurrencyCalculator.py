print("enter the value of currency")
currency= int(raw_input())
print("No. of 500 Note: "+str(currency/500))
currency=currency%500

print("No. of 100 Note: "+str(currency/100))
currency=currency%100

print("No. of 50 Note: "+str(currency/50))
currency=currency%50

print("No. of 20 Note: "+str(currency/20))
currency=currency%20

print("No. of 10 Note: "+str(currency/10))
currency=currency%10

print("No. of 5 Note: "+str(currency/5))
currency=currency%5

print("No. of 2 Note: "+str(currency/2))
currency=currency%2

print("No. of 1 Note: "+str(currency/1))
currency=currency%1
