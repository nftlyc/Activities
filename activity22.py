# My python function

def Greetings():
    print("Hello Everyone")

def activity1():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            print ("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b\b\b*******\n\t\t\t\t\t\t\t\b\b*****\n\t\t\t\t\t\t\t\b***\n\t\t\t\t\t\t\t*")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")
        
def activity2():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            name = input ("Please type your name ==> ")

            print("Hi" +  name) 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity3():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            fullname = input (" What is your name? ")
            age = input (" How old are you? ")
            mobilenumber = input (" What is your mobile number? ")
            email = input (" Email: ")
            gender = input (" Sex: ")
            dateofbirth = input (" Date of birth: ")
            placeofbirth = input (" Where were you born? ")
            maritalstatus = input (" Is married? true or false ")
            religion = input (" Religion: ")
            languagesknown = input (" Languages known: ")
            address = input (" Address: ")

            print ("Hi, my name is " + fullname + " and I'm " , age , " years old " , gender , " \nI live in " + address + " \nmy phone number is " , mobilenumber , " and this is my email " + email + " \nI was born on " , dateofbirth , " in " + placeofbirth + " \nIt is " , maritalstatus ," that i'm married \nMy religion is " + religion + " and " + languagesknown + " is tha language that i can speak")

    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity4():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            number1 = eval(input("Enter a number ---> "))
            number2 = eval(input("Enter another number ---> "))
            answer = (number1 + number2)

            print(f"The sum of {number1} and {number2} is {answer}")
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity5():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

            print("=======================================")

            fahrenheit = eval(input("Enter temperature in Fahrenheit ----> "))

            celsius = ((fahrenheit - 32)*5) / 9

            print(f"{fahrenheit} degrees Fahrenheit converted to celsuis is {celsius} degrees")
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity6():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            x = 5

            print(x)

            x = x + 10

            print(x)

            x = x + 15

            print(x)

            x += 10

            print(x)

            x += 20

            print(x)
        else:
            print("Invalid answer, pls only answer 'yes' or 'no'")

def activity7():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            gold = 0

            name = input("Hi, Enter your name: ")
            hasMine = input("Did you mine gold today? ")

            if hasMine.lower() == "yes":
                gold += hasMine
                print(f"Hi! {name}, Today you have a total of {gold} gold")
            else:
                print(f"Hi! {name}, Today you have a total of {gold} gold")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity8():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            password = input("Enter your password: ")

            if password.lower() == "neftalycareg420":
                print("Acces Granted")
                print("Enjoy using the system")
            elif password.lower() == "neftalycareg123":
                print("Acces Granted")
                print("Enjoy using the system")
            else:
                print("Acces Denied")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity9():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            age = eval(input("Enter your age here ---> "))

            if age <= 7 and age >= 1:
                print("You are a Toddler")

            elif age <= 13 and age >= 8:
                print("You are a Pre-Teen")

            elif age <= 18 and age >= 14:
                print("You are a Teenager")

            elif age <= 31 and age >= 19:
                print("You are in a Early Adulthood")

            elif age <= 45 and age >= 32:
                print("You are in a Mid Adulthood")

            elif age <= 59 and age >= 46:
                print("You are in a Mid Adulthood")

            elif age <= 100 and age >= 60:
                print("You are in a Mid Adulthood")

            else:
                print("Please enter a number") 
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity10():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            name = input("Enter your name: ")
            isStudent = input("Are you a current student of DLL (YES) or (NO): ")

            if isStudent.lower() == "yes":
                yearlevel = input("What year are you currently enrolled? \nF - Freshmen \nS - Sophomore \nJ - Junior \nSR - Senior \nPlease input your answer here: ")

                if yearlevel.lower() == "f":
                    print(f"Hi {name}, Freshmen, Welcome to DLL!")
                if yearlevel.lower() == "s":
                    print(f"Hi {name}, Sophomore, Welcome to DLL!")
                if yearlevel.lower() == "j":
                    print(f"Hi {name}, Junior, Welcome to DLL!")
                if yearlevel.lower() == "sr":
                    print(f"Hi {name}, Senior, Welcome to DLL!")
                else:
                    print("Invalid Input")
        
            else:
                print(f"Thankyou for using the system")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity11():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
                for IKOT in range (1,10):
                    print("Hello World")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity12():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for bilang in range (10, 1, -1):
                print(f"wow ganto sya kadami {bilang}")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity13():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            sum = 1
            isa = int(input("Enter a number: "))
    
            for x in range (isa,0,-1):
                sum *= x
            print(f"The factorial of {isa} is {sum}")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity14():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range (0, 11):
                print(x, end= " ")
                for y in range (0, 11):
                    print("*", end= " ")
            print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity15():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            for x in range (0, 11):
                print(x, end= " ")
                for y in range (0, x):
                    print("*", end= " ")
            print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity16():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
                for x in range (1,11):
                    for y in range(1,x+1):
                        print(" ",end=" ")
                    for z in range(11,x,-1):
                        print("*",end=" ")
                    print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity17():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            column = eval(input("Enter number of column >>> "))
            for x in range(1,11):
                for y in range(1,column + 1):
                    print(x*y,end="\t")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity18():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            nt = eval(input("Enter number of triangle(s) ==> "))
            for x in range(1,5):
                for y in range(1,nt+1):
                    for z in range(1,x+1):
                        print("*",end=" ")
                    for a in range(5,x,-1):
                        print(" ",end=" ")
                    print(end=" ")
                print()
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity19():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True

            while tuloy:
                name = input("Enter your name: ")
                if name.lower() == "stop":
                    print("PROGRAM TERMINATED")
                    break
                    tuloy = False
                else:
                    continue
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity20():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            total = 0
            ilan = 0
            while tuloy:
                namba = int(input("Pls enter a number --> "))
                if namba == 0:
                    print("Loop has now terminated")
                    print(f"You have entered {ilan} numbers")
                    print(f"The sum of all the numbers given is {total}")
                    break
                ilan += 1
                total += namba
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")

def activity21():
    tuloy = True

    while tuloy:
        ask = input("Do you wish to run the program (yes or no) -> ")

        if ask.lower() == "no":
            print("Program Terminated")
            break
        elif ask.lower() == "yes":
            tuloy = True
            num = 0

            while tuloy:
                ask = input("Do you wish to create a new triangle (yes or no) -> ")

                if ask.lower() == "no":
                    print("Program / Loop Terminated")
                    break
                elif ask.lower() == "yes":
                    num += 1
                    for x in range(1,6):
                        for a in range(1,num + 4):
                            for y in range(1,x+1):
                                print(y,end=" ")
                            for z in range(6,x,-1):
                                print(" ",end=" ")
                        print()
                    continue
            else:
                print("Invalid answer, pls only answer 'yes' or 'no'")
    else:
        print("Invalid answer, pls only answer 'yes' or 'no'")


isContinue = True

while isContinue:
    print("SELECT FROM THE FOLLOWING CODE \n1 = activity1 \n2 = activity2 \n3 = activity3 \n4 = activity4 \n5 = activity5 \n6 = activity6 \n7 = activity7 \n8 = activity8 \n9 = activity9 \n10 = activity10 \n11 = activity11 \n12 = activity12 \n13 = activity13 \n14 = activity14 \n15 = activity15 \n16 = activity16 \n17 = activity17 \n18 = activity18 \n19 = activity19 \n20 = activity20 \n21 = activity21")

    ask = input("Which program would you like to run?, Please select from the option above, Enter Here ==> ")

    if ask == "1":
        activity1()
        continue

    elif ask == "2":
        activity2()
        continue

    elif ask == "3":
        activity3()
        continue

    elif ask == "4":
        activity4()
        continue

    elif ask == "5":
        activity5()
        continue

    elif ask == "6":
        activity6()
        continue

    elif ask == "7":
        activity7()
        continue

    elif ask == "8":
        activity8()
        continue

    elif ask == "9":
        activity9()
        continue

    elif ask == "10":
        activity10()
        continue

    elif ask == "11":
        activity11()
        continue

    elif ask == "12":
        activity12()
        continue

    elif ask == "13":
        activity13()
        continue

    elif ask == "14":
        activity14()
        continue

    elif ask == "15":
        activity15()
        continue

    elif ask == "16":
        activity16()
        continue

    elif ask == "17":
        activity17()
        continue

    elif ask == "18":
        activity18()
        continue

    elif ask == "19":
        activity19()
        continue

    elif ask == "20":
        activity20()
        continue

    elif ask == "21":
        activity21()
        continue

    elif ask == "stop":
        print("The Program Terminated")
        print("Thankyou for using the system!")
        break

    


