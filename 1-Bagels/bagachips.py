import random
import pdb

MAX_TRIES = 10
NUM_DIGITS = 3

def main():
    print('This is the game, guess a number of {} digits'.format(NUM_DIGITS))
    while True: 
        tries = 1
        secret_numa = getSecretNuma(NUM_DIGITS)
        print('You have {} guesses to get it.'.format(MAX_TRIES))
        while (tries <= MAX_TRIES):
            print ("Try number[{}]:".format(tries))
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                guess = input(">")

            clues = getClues(secret_numa, guess)
            print (clues)

            tries += 1

            if (guess == secret_numa):
                break

            if (tries > MAX_TRIES):
                print("Sorry you loose")
                break
        
        if not playAgain():
            break

    print ("Thanks for playing")
    

# play again
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input(">").lower().startswith('y')

# funciones auxiliares
def getSecretNuma(max):
    secret_num = ""
    for _ in range(max):
        secret_num += str(random.randint(0, 9))
    return secret_num

def getClues(secret_numa, guess):
    clues = []
    i = 0

    if guess == secret_numa:
        return ["YOU WIN!"]

    for digit in guess:
        if digit == secret_numa[i]:
            clues.append("FERMI")
        elif digit in secret_numa:
            clues.append("PICO")
        i += 1
    
    if (len(clues) == 0):
        return ["BAGA"]
    clues.sort()

    return clues
        

# main when running directly
if __name__ == '__main__':
    main()