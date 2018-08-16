"""Dice Rolling game
prompts for a guess
evaluates and gives a response
"""


import random

win=0
loss=0
def rollDice(win,loss):
    random.seed()    #So the generated number is different in each instance
    num = random.randrange(1,6)


    guess = int(input('Guess a number in the range 1-6: '))

    if num==guess:
        print('You have guessed correctly the answer is: ',num)
        win+=1
    else:
        print('you have guessed incorrectly the correct answer is: ', num)
        loss+=1

    choice = input(' would you like to play again \n Y for yes any other character for no: ')
    
    if choice == 'Y' or choice == 'y':
        rollDice(win,loss)

    print('you have won: ', win, 'games')
    print('you have lost: ',loss, 'games')
    return    

rollDice(win,loss)
