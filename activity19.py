tuloy = True

while tuloy:
    name = input("Enter your name: ")
    if name.lower() == "stop":
        print("PROGRAM TERMINATED")
        break
        tuloy = False
    else:
        continue