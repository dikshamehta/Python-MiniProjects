try:
    no1= int(input("enter first number: "))
    no2= int(input("enter second number: "))
    res=no1/no2

except ValueError:
    print("wrong value input")

except ZeroDivisionError:
    print("can not divide by zero")

except:
    print("something wrong has happened")

else:
    print("answer:"+str(res))

finally:
    print("this will work in any situation")
