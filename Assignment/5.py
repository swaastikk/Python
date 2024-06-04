a = int(input("first value = "))
b = int(input("second value = "))
add = int(a+b)
product = int(a*b)
if(a>b):
    sub = int(a-b)
    div = int(a/b)
else:
    sub = int(b-a)
    div = int(b/a)
    
print("addition = ", add)
print("substraction = ", sub)
print("multiplication = ", product)
print("division = " ,div)