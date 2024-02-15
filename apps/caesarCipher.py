# data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z']


def encrypt(text, shift):
    text_list = list(text)
    text_data = []

    # make an alphabet data list from text
    for letter in text_list:
        count = 0
        for i in letters:
            if i == letter:
                text_data.append(count)
                break
            count += 1

    # shift every number by given value and print it to a different list
    sh_number_data = []
    for i in text_data:
        sh_number = i + shift
        sh_number_data.append(sh_number)

    # turn shifted number data into alphabet data
    sh_text_data = []
    for i in sh_number_data:
        sh_text_data.append(letters[i])

    encrypted_string = ""
    print("Encrypted text:")
    print(encrypted_string.join(sh_text_data))


def decrypt(text, shift):
    text_list = list(text)
    text_data = []

    # make an alphabet data list from text
    for letter in text_list:
        count = 0
        for i in letters:
            if i == letter:
                text_data.append(count)
                break
            count += 1

    # shift every number back by given value and print it to a different list
    sh_number_data = []
    for i in text_data:
        sh_number = i - shift
        sh_number_data.append(sh_number)

    # turn shifted number data into alphabet data
    sh_text_data = []
    for i in sh_number_data:
        sh_text_data.append(letters[i])

    encrypted_string = ""
    print("Decrypted text:")
    print(encrypted_string.join(sh_text_data))


def auto_decrypt(text, iteration):
    text_list = list(text)
    text_data = []

    # make an alphabet data list from text
    for letter in text_list:
        count = 0
        for i in letters:
            if i == letter:
                text_data.append(count)
                break
            count += 1

    for iteration in range(0, iteration):
        # shift every number by given value and print it to a different list
        sh_number_data = []
        for i in text_data:
            sh_number = i - (iteration + 1)
            sh_number_data.append(sh_number)

        # turn shifted number data into alphabet data
        sh_text_data = []
        for i in sh_number_data:
            sh_text_data.append(letters[i])

        encrypted_string = ""
        print(f"{iteration + 1}. iteration")
        print(encrypted_string.join(sh_text_data))


print("Text Encrypt/Decrypt Program 1.0v")
userInput = input("Do you want to encrypt, decrypt or auto-decrypt (e, d, au): ")

if userInput == "e":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypt(text, shift)
elif userInput == "d":
    text = input("Enter text to decrypt: ")
    shift = int(input("Enter shift value: "))
    decrypt(text, shift)
elif userInput == "au":
    text = input("Enter text to decrypt: ")
    iteration = int(input("Enter the number of iteration: "))
    auto_decrypt(text, iteration)
else:
    print("Please enter a valid input")


# take text, turn it into a list
# find corresponding numbers in the alphabet and print the data into another list
# change the numbers by shift number
# turn them into alphabet again
