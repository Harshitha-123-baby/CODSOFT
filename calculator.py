def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def moddivision(a,b):
    return a%b
def division(a,b):
    return a/b
while(True):
    print("menu:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.ModDivision\n5.Division\n")
    choice=int(input("enter your choice(1-5):"))     
    if(choice==1):
        a=int(input("enter value of a:"))
        b=int(input("enter value of b:"))
        print("addition of a and b:",addition(a,b))
    elif(choice==2):
        a=int(input("enter value of a:"))
        b=int(input("enter value of b:"))
        print("subtraction of a and b:",subtraction(a,b))
    elif(choice==3):
        a=int(input("enter value of a:"))
        b=int(input("enter value of b:"))
        print("multiplication of a and b:",multiplication(a,b))
    elif(choice==4):
        a=int(input("enter value of a:"))
        b=int(input("enter value of b:"))
        print("moddivision of a and b:",moddivision(a,b))
    elif(choice==5):
        if(b!=0):
            a=int(input("enter value of a:"))
            b=int(input("enter value of b:"))
            print("division of a and b:",division(a,b))
        else:
            print("Division with zero")
    else:
        print("invalid choice")
        break
