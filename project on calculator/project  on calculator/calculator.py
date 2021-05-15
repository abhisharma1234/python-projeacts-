from function import *


print("Hi! Welcome To Calculator")
print("What You Want To Do?")
print(" 1: Addition ")
print(" 2: subtraction ")
print(" 3: multiplication")
print(" 4: division")
print(" 5: Root")
print(" 6: power")
choice=input("enter choice:")
if choice=='1':
    Num1 = float(input("Enter first number"))
    Num2 = float(input("Enter second number"))
    addition(Num1,Num2)
elif choice=='2':
    Num1 = float(input("Enter first number"))
    Num2 = float(input("Enter second number"))
    difference(Num1,Num2)
elif choice=='3':
    Num1 = float(input("Enter first number"))
    Num2 = float(input("Enter second number"))
    multiplication(Num1,Num2)
elif choice=='4':
    Num1 = float(input("Enter first number"))
    Num2 = float(input("Enter second number"))
    division(Num1, Num2)
elif choice=='5':
    Num1 = int(input("entr the number"))
    Root(Num1)
else:
    if choice =='6':
        Num1 = int(input("enter the number"))
        Num2 = int((input("enter the power number")))
        power(Num1,Num2)




