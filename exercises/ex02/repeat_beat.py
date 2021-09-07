"""Repeating a beat in a loop."""

__author__ = " 730449914"

Counter: int = 0
beat: str = str(input("What beat do you want to repeat? "))
frequence: int = int(input("How many times do you want to repeat it? "))

if frequence > 0:
    while Counter < frequence:
        if Counter < frequence - 1:
            print(beat + " ", end="")
        else:
            print(beat)
        Counter = Counter + 1
else:
    print("No beat...")