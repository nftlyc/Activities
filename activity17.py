column = eval(input("Enter number of column >>> "))
for x in range(1,11):
    for y in range(1,column + 1):
        print(x*y,end="\t")
    print()