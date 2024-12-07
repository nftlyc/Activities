nt = eval(input("Enter number of triangle(s) ==> "))
for x in range(1,5):
    for y in range(1,nt+1):
        for z in range(1,x+1):
            print("*",end=" ")
        for a in range(5,x,-1):
            print(" ",end=" ")
        print(end=" ")
    print()