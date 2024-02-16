import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?']

print("Password Generator 1.0v")
length = int(input("Enter password length: "))
scale = int(input("Enter the incomprehensibility level (1, 2, 3): "))
if not 1 <= scale <= 3:
    print("Please enter a valid input")
    quit()

password = []
for i in range(0, length):
     password.append(random.choice(letters))

multiplier2 = round(length / 6)
multiplier3 = round(length / 2)

if scale == 2:
    for i in range(0, multiplier2):
        selectedElementNum = random.choice(numbers)
        selectedElementSym = random.choice(symbols)
        randomIndexNum = random.randint(0, len(password) - 1)
        randomIndexSym = random.randint(0, len(password) - 1)

        password[randomIndexNum] = selectedElementNum
        password[randomIndexSym] = selectedElementSym
elif scale == 3:
    for i in range(0, multiplier3):
        selectedElementNum = random.randint(0, len(numbers) - 1)
        selectedElementSym = random.randint(0, len(symbols) - 1)
        randomIndexNum = random.randint(0, len(password) - 1)
        randomIndexSym = random.randint(0, len(password) - 1)

        password[randomIndexNum] = numbers[selectedElementNum]
        password[randomIndexSym] = symbols[selectedElementSym]

printPassword = ""
printPassword = printPassword.join(password)

print(printPassword)