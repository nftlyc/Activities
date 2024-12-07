name = input("Enter your name: ")
isStudent = input("Are you a current student of DLL (YES) or (NO): ")

if isStudent.lower() == "yes":
    yearlevel = input("What year are you currently enrolled? \nF - Freshmen \nS - Sophomore \nJ - Junior \nSR - Senior \nPlease input your answer here: ")

    if yearlevel.lower() == "f":
        print(f"Hi {name}, Freshmen, Welcome to DLL!")
    elif yearlevel.lower() == "s":
        print(f"Hi {name}, Sophomore, Welcome to DLL!")
    elif yearlevel.lower() == "j":
        print(f"Hi {name}, Junior, Welcome to DLL!")
    elif yearlevel.lower() == "sr":
        print(f"Hi {name}, Senior, Welcome to DLL!")
    else:
        print("Invalid Choice")
        
else:
    print(f"Thankyou for using the system")