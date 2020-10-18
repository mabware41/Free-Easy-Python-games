import random
min = 1
max = 6

roll_again: str = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_me_again = input("Would you like to roll again? Enter 'y' or 'n' ")

    if roll_me_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for using me!")
        break
