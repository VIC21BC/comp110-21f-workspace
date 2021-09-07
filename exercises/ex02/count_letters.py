"""Counting letters in a string."""

__author__ = "730449914"


letter: str = str(input("What letter do you want to seach for?: "))
word: str = str(input("Enter a word: "))

i: int = 0
Counter: int = 0

while i < len(word):
    if word[i] == letter:
        Counter = Counter + 1
    i = i + 1
print("Count: " + str(Counter))