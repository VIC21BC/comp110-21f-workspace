"""Finding duplicate letters in a word."""

__author__ = "730449914"


word: str = str(input("Enter a word: "))

i: int = 0
f: bool = False

while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            f = True
        j = j + 1
    i = i + 1

print("Found duplicate: " + str(f))
       
