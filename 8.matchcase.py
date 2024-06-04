x = int(input("Enter the value = "))
match x:
    case 0 :
        print("ZERO")
    case 10 :
        print("TEN")
    case _ if x!=90:
        print("NOT 90")
    case _ if x!=100:
        print("NOT 100")
    case _ :
        print(x)  