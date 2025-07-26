#calculator project
def add():
    return num1 + num2
def subtract():
    return num1 - num2
def multiplication():
    return num1 * num2
def divide():
    return num1/num2

num1 = int(input("enter your first number:"))
opreator = input("selcet your option:")
num2 = int(input("enter your second number:"))

if opreator == "+":
    print(add())

elif opreator == "-":
    print(subtract())

elif opreator == "*":
    print(multiplication())

elif opreator == "/":
    print(divide())

else:
    print("invalid opreation that can not perform")
    
