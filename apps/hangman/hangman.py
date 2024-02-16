import random

# data
words = ['basic',
         'credit',
         'red',
         'quotation',
         'widen',
         'marsh',
         'precedent',
         'value',
         'heal',
         'fight',
         'width',
         'dedicate']

# examine selected word
selectedWord = random.choice(words)
listWord = list(selectedWord)
letterPool = []

for letter in listWord:
    # check if letter already exists in the letterPool
    isUnique = True
    for i in letterPool:
        if letter == i:
            isUnique = False

    # assign it if it's unique
    if isUnique:
        letterPool.append(letter)

# initial graphics
displayWord = []
for i in listWord:
    displayWord.append("_")

leftLives = 10


def displayhangman():
    if leftLives == 10:
        print('''
                   
                   
                   
                   
                   
                   
        ''')
    elif leftLives == 9:
        print('''
                   
                   
                   
                   
                   
               A
        ''')
    elif leftLives == 8:
        print('''
               
               | 
               | 
               | 
               | 
               A
        ''')
    elif leftLives == 7:
        print('''
               _____
               | 
               | 
               | 
               | 
               A
        ''')
    elif leftLives == 6:
        print('''
               _____
               |   |
               | 
               | 
               | 
               A
        ''')
    elif leftLives == 5:
        print('''
               _____
               |   |
               |   0
               | 
               | 
               A
        ''')
    elif leftLives == 4:
        print('''
              _____
              |   |
              |   0
              |   |
              |    
              A
        ''')
    elif leftLives == 3:
        print('''
              _____
              |   |
              |   0
              |  /|
              |  
              A
        ''')
    elif leftLives == 2:
        print('''
              _____
              |   |
              |   0
              |  /|\\
              |  
              A
        ''')
    elif leftLives == 1:
        print('''
              _____
              |   |
              |   0
              |  /|\\
              |  /
              A
        ''')


# configurations
usedLetters = []
guessedLetters = []
displayString = ""

print("Hangman 1.0v")
print("Start?")
input()

isGameOver = False
while not isGameOver:
    # display hangman interface
    displayhangman()

    print(displayString.join(displayWord))
    pickedLetter = input("Guess a letter: ")

    leftLives -= 1
    for letter in letterPool:
        if letter == pickedLetter:
            guessedLetters.append(pickedLetter)
            leftLives += 1
        else:
            usedLetters.append(pickedLetter)

    index = 0
    for letter in listWord:
        if letter == pickedLetter:
            displayWord[index] = pickedLetter
        index += 1

    # game over checker
    checkWin = True
    checkLoss = True
    for letter in displayWord:
        if letter == '_':
            checkWin = False
            break

    if leftLives > 0:
        checkLoss = False

    if (checkWin or checkLoss):
        isGameOver = True

if checkLoss:
    print('''
          _____
          |   |
          |   0
          |  /|\\
          |  / \\
          A
          
    Game over, you lost.
    ''')
elif checkWin:
    print(f"The word was: {displayString.join(displayWord)}")
    print("You won!")
