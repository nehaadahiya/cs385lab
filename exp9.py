#Aim= to demonstrate error handling
try:
    a=int(input("enter the number: "))
    print(a/2)
    print(a/0)
except(ArithmeticError, ValueError):
    print("An error Occoured\n")