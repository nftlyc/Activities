sum = 1
isa = int(input("Enter a number: "))

for x in range (isa,0,-1):
    sum *= x
print(f"The factorial of {isa} is {sum}")
