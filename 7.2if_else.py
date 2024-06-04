num = int(input("Enter the number = "))
if(num<0):
    print("NEGATIVE NUMBER")
elif(num>0):
    print("POSITIVE NUMBER")
    if(num<=10):
      print("number is between 1 to 10")
    elif(num>10 and num<=50):
        print("number is between 10 to 50")
    else:
        print("number is greater than 50")
else:
    print("ZERO")