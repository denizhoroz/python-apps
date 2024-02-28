import random

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?']

    password = []

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
        password.append(random.choice(letters))

    for sym in range(nr_symbols):
        password.append(random.choice(symbols))

    for num in range(nr_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)
    printPassword = ""
    printPassword = printPassword.join(password)

    return printPassword

