"""Challenge question #1"""

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")

def vic():
    word: str = str(input("Enter a word "))
    i: int = 0
    x: int = 0

    while i < len(word):
        while x < len(word):
            if x == i and (x + 1) < len(word):
                x = x + 1
            else:
                if (i + 1) == len(word):
                    return False
                else:
                    if word[i] == word[x]:
                        return True
                    else:
                        x = x + 1
    i = x + 1
    x = 0
    x = x + i