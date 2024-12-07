gold = 0

name = input("Hi, Enter your name: ")
hasMine = input("Did you mine gold today? ")

if hasMine.lower() == "yes":
    gold += 1
    print(f"Hi! {name}, Today you have a total of {gold} gold")
else:
    print(f"Hi! {name}, Today you have a total of {gold} gold")
