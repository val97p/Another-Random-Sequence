list = [1, 5, 12, 22, 35]
print(list)

next_number = int(input("what's the next number? "))

while next_number != 51:
    print("That's not the answer ")
    print("Try again")
    next_number = int(input("What's the next number?"))
    hint_question = input("Do you want a hint? ")
    if hint_question == "yes":
        print("Pentagonal")
        next_number = int(input("What's the next number?"))
    else:
        next_number = int(input("What's the next number?"))
else:
    list.append(next_number)
    print(list)

next_number1 = int(input("what's the next number? "))

while next_number1 != 70:
    print("That's not the answer ")
    print("Try again")
    next_number1 = int(input("What's the next number?"))

else:
    list.append(next_number1)
    print(list)


next_number2 = int(input("what's the next number? "))

while next_number2 != 92:
    print("That's not the answer ")
    print("Try again")
    next_number2 = int(input("What's the next number?"))
else:
    list.append(next_number2)
    print(list)

next_number3 = int(input("What's the next number?"))
while next_number3 != 117:
    print("That's not the answer ")
    print("Try again")
    next_number3 = int(input("What's the next number?"))

else:
    list.append(next_number3)
    print(list)

next_number4 = int(input("What's the next number?"))
while next_number4 != 145:
    print("That's not the answer ")
    print("Try again")
    next_number4 = int(input("What's the next number?"))

else:
    list.append(next_number4)
    print(list)