import random
import math

lower = int(input("Enter Lower Bound "))

upper = int(input("Enter Upper Bound "))

x = random.randint(lower, upper)
print(
    f"\n\tYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print(f"Congratulation you did it in {count} try")
        break
    elif x > guess:
        print("You guess too small!")
    elif x < guess:
        print("You guessed to high!")

if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d " % x)
    print("\t Better Luck Next time!")
