"""Coin guess and math game!"""

__author__ = "730449914"

from random import randint

points: int = 1
player: str  
NAMED_CONSTANT: str = '\U0001F600'
NAMED_CONSTANT_1: str = '\U0001F62A'


def greet() -> None:
    """Welcome message!"""
    print(f"Welcome stranger! You have now entered the game {NAMED_CONSTANT}.")
    global player
    player = (input("Please enter your name: "))


def math(b: int, c: int) -> int:
    """Multiplication function!"""
    global player
    yes_no = input(f"You are now inside the powerful calculator {player}. Are you sure that you want to continue? ")
    if len(yes_no) > 2:
        print("I love your courage!")
    else:
        print("Haha it is already too late, the powerful calculator can't be stopped now!")
    
    return b * c


def coin() -> None:
    """Coin function."""
    global player
    global points
    print(f"You have now entered the coin game {player}. Your goal is to guess wheater the coin will land heads (1) or tails (2). To win, you need to guess right three times in a row.")
    print(f"One correct answer will give you five points. If you win the game, you will gain 50 - 150 points. However, if you guessed incorrectly, you will lose all your points. Good luck!{NAMED_CONSTANT}")
    a: int = 0
            
    while a < 3:
        guess: str = input("Enter your guess: ")

        if randint(1, 2) == int(guess):
            print("You guessed correct!")
            points = points + 50
            a = a + 1
               
        else:
            print(f"You guessed incorrectly {NAMED_CONSTANT_1}. Try again")
            points = a * (-5)
            a = 0


def main() -> None:
    """This is the important function!"""
    global player
    global points
    greet()
    i: int = 1
    
    while i > 0:
        print(f"You are now in the game lobby {player}, at this moment you have {points} points. You have the following choices!")
        print("Coin game: Enter 1. Math game: Enter 2. Quit the game: Enter 3")
        choice: str = input("Enter one of the numbers to continue: ")
    
        if 1 == int(choice):
            coin()
            print(f"You are a superstar {player}")
            print(f"At this moment you have {points} points.")
        else:
            if 2 == int(choice):
                print(f"You have now entered the math game {player}. In this game, you will encounter multiplication questions. You will multiply your current points with a value of your choice. If you guessed correctly, the total sum will be added to your points. However, if you guess incorrectly, your points will stay the same. Good luck!")
                qop: int = int(input("if you want to play one round of the game, Enter 1. If you want to go back to lobby, Enter 2: "))

                while 1 == int(qop):
                    print(f"At this moment you have {points} points.")
                    n_1: int = int(input("Enter the number you want to multiply your points with: "))
                    print(f"At this moment you have {points} points.")
                    answer: str = input(f"What is {points} * {n_1}? ")

                    if int(answer) == math(int(n_1), int(points)):
                        print(f"{player}, you guessed correctly {NAMED_CONSTANT}. You answered {answer} and the correct answer was {math(int(n_1), int(points))}!")
                        points = points + (n_1 * points)
                        con: str = input("If you want to play one more round of the game, enter 0. If you want to go back to lobby, Enter 1: ")
                        qop = qop + int(con)
                    else:
                        print(f"You guessed incorrectly {NAMED_CONSTANT_1}. You answered {answer} and the correct answer was {math(int(n_1), int(points))}")
                        con_1: str = input("If you want to play one more round of the game, enter 0. If you want to go back to lobby, Enter 1: ")
                        qop = qop + int(con_1)
            else:
                i = 0
        

if __name__ == "__main__":
    main()