"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730225319"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

random_num: int = randint(1,4)

if random_num == 1:
    print("You will find happiness in the most underrated aspects of life! :)")
else:
    if random_num == 2:
        print("Success, however you define it, is coming your way! :)")
    else:
        if random_num == 3:
            print("Someone who you will love for the rest of your life will come your way. ;)")
        else:
            print("You will accomplish your goals soon! :)")

print("Now, go spread positive vibes!")