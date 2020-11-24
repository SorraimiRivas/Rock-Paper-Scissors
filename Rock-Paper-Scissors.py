#Rock-Paper-Scissors

import time
import random

#Loop and AI values

def startGame():
    AIplay = random.randint (1, 3)

    if AIplay == 1:
        AIplay = 'Rock'
    if AIplay == 2:
        AIplay = 'Paper'
    else:
        AIplay = 'Scissors'

    print ('Please input your play (Rock, Paper or Scissors)')
    playerInput = input()
    print()
    time.sleep(1)
    print(f"AI's play is {AIplay}.")
    print()

    #Game Behavior

    def gamePlay():
        if AIplay == playerInput:
            print("It's a DRAW")
                
        if AIplay == 'Rock' and playerInput == 'Paper':
            print (f'{playerInput} wins over {AIplay} ')
            time.sleep(1)
            print()
            print('Player WINS!')

        if AIplay == 'Paper' and playerInput == 'Scissors':
            print (f'{playerInput} wins over {AIplay}')
            time.sleep(1)
            print()
            print ('Player WINS!')
        
        if AIplay == 'Scissors' and playerInput == 'Rock':
            print (f'{playerInput} wins over {AIplay}')
            time.sleep(1)
            print()
            print ('Player WINS!')
        
        else:
            print(f'{AIplay} wins over {playerInput}')
            time.sleep(1)
            print()
            print ('AI WINS!')

    gamePlay()

playAgain = 'yes'

while playAgain == 'yes':
    startGame()
    print()
    print('Do you want to play again? (yes or no)')
    playAgain = input()



