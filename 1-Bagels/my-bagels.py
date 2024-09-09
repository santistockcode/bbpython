import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
          This is how it is played:

I am thinking of a {}-digit number with no repeated digits.
and so on..'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess numa{}: '.format(numGuesses))
                guess = input(':: ')

            clues = getClues(guess, secretNum)

            print(clues)

            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print ('You ran out of guesses.')
                print ('The answer was {}'.format(secretNum))

        print ('Do you wanna play again')
        if not input('> ').lower().startswith('y'):
            break
    print ('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('PICO')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
    



# If the program is run instead of imported, run the game: 
if __name__ == '__main__':
    main()