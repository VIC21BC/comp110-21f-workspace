"""Drawing forests in a loop."""

__author__ = "730449914"


depht: int = int(input("Depht: "))
i = 1
TREE: str = '\U0001F332'

if depht > 0:
    while i <= depht:
        print(i * TREE)
        i = i + 1