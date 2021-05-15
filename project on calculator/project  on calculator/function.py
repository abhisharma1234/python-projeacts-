import math

def addition(Num1,Num2):
    result = Num1 + Num2
    print("sum of {} and {} is {}".format(Num1, Num2, result))

def difference(Num1,Num2):
    result = Num1 - Num2
    print("difference betwween {} and {} is {}".format(Num1, Num2, result))


def multiplication(Num1,Num2):
    result = Num1 * Num2
    print("multiple of {} and {} is {}".format(Num1, Num2, result))

def division(Num1,Num2):
    if Num2 == '0':
        print("can't divide by 0")
    else:
        result = Num1 / Num2
        print("divide of {} and {} is {}".format(Num1, Num2, result))

def Root(Num1):
    if Num1 < 0:
        print("please enter +ve value")
    else:
        result = math.sqrt(Num1)
        print("the square root of {} is {}".format(Num1, result))

def power(Num1,Num2):
    result = (Num1**Num2)
    print("the number {} to the power {} is {}".format(Num1, Num2, result))