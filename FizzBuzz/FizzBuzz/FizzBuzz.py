#Fizz Buzz game written in Python 3
#Dan French - 2018

#Function to display the initial splash screen
def Splash():
    print('Welcome to FizzBuzz')
    print('')
    Menu()

#Function to display the user menu
def Menu():
    startChoice = input('Enter S to start, R for rules or E to exit: ')
    if (startChoice.upper() == 'S'):
        StartGame()
    elif (startChoice.upper() == 'R'):
        DisplayRules()
    elif (startChoice.upper() == 'E'):
        exit()
    else:
        print('invalid choice')
        Menu()

#Function to display the game rules, printed to screen
def DisplayRules():
    print('')
    print('   You are playing against the computer and each take turns')
    print('   The game starts with 1 and increments each turn')
    print('   If the number is divisible by 3 you type Fizz')
    print('   If the number is divisible by 5 you type Buzz')
    print('   If the number is divisible by 3 and 5 you type FizzBuzz')
    print('')
    Menu()

#Function used for gameplay
def StartGame():
    alive = True    #setting to false ends game
    count = 1       #used to keep track of number
    while (alive == True):
        if (count % 2 == 0):
            print (CheckNum(count))
        else:
            playerInput = input('')
            playerCheck = CheckNum(count)
            if (playerInput.upper() != playerCheck.upper()):
                print('Game Over')
                alive = False
        count += 1

#Function to check if a number is divisible by 3, 5 or both
#Param num - int, the number for checking
#Returns string
def CheckNum(num):
    if (num % 5 == 0 and num % 3 == 0):
        return 'FizzBuzz'
    elif (num % 5 == 0):
        return 'Buzz'
    elif (num % 3 == 0):
        return 'Fizz'
    else:
        return str(num)

#Application start point

Splash()
