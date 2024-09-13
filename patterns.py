print(""" PATTERNS MENU
1.Increament Triangle Pattern
2.Decremant Triangle Pattern
3.Pyramid/Hill Pattern
4.Reverse Pyramid/Hill Pattern
5.Diamond Pattern
6.Square pattern""")
choice=0
while (choice>=0 and choice <= 6):
    choice=int(input("Enter pattern type:"))
    #Increment triangle Pattern
    if (choice == 1):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(size):
            for j in range(i+1):
                print(data,end=" ")
            print()
    #Decrement triangle Pattern
    elif (choice == 2):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(size):
            for j in range(i,size):
                print(data,end=" ")
            print()
    #Pyramid/Hill Pattern 
    elif (choice == 3):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(1,size+1):
            for j in range(1,size-i+1):
                print(" ",end=" ")
            for j in range(1,2*i):
                print(data,end=" ")
            print()
    #Reverse Pyramid/Hill Pattern
    elif (choice == 4):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(size,0,-1):
            for j in range(1,size-i+1):
                print(" ",end=" ")
            for j in range(1,2*i):
                print(data,end=" ")
            print()
    #Diamond using symbol
    elif (choice == 5):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(1,size+1):
            for j in range(1,size-i+1):
                print(" ",end=" ")
            for j in range(1,2*i):
                print(data,end=" ")
            print()
        for i in range(size-1,0,-1):
            for j in range(1,size-i+1):
                print(" ",end=" ")
            for j in range(1,2*i):
                print(data,end=" ")
            print()
    elif(choice==6):
        size=int(input("Enter rows:"))
        data=input("Enter data:")
        for i in range(size):
            for j in range(size):
                print(data,end=" ")
            print()
    else:
        print("Invalid choice")
    


