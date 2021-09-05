"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730449914"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

number: int = 1

print("Your fortune cookie says...")
if randint(1, 10) == 1:
    print("You will soon find the love of your life!")
else:
    if randint(1, 10) < 3:
        print("Riches are waiting around the corner!")
    else: 
        if randint(1, 10) > 5:
            print("Believe in yourself and you will succeed!")
        else:
            if randint(1, 10) > 8:
                print("Something exciting is going to happen to you soon!")

print("Now, go spread positive vibes!")