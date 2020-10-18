import random

num = random.randint(1, 25)

guesses = [0]

while True:
    guess = int(input("im thinking of a number between 1 and 25.\n whats your guess?"))

    if guess < 1 or guess > 25:
        print('out of bounds! pls try again:')
        continue

    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('warmer')
        else:
            print('colder')
    else:
        if abs(num - guess) <= 10:
            print('warm')
        else:
            print('cold')



