"""Coin guess!"""

from random import randint

points: int 
player: str  
NAMED_CONSTANT: str = '\U0001F332'


def greet() -> None:
    global player
    player: str = (input(f"Welcome stranger! You have now entered the game{NAMED_CONSTANT}. Please enter your name: "))


def math(b: int, c: int) -> int:
    return b * c


def main() -> None:
    global player
    global points
    greet()
    i: int = 1
    
    while i > 0:
        print(f"You are now in the game lobby{player}, at this moment you have {points} Points. Click enter to see your Choices!")
        print("Coin game: Enter 1. Math game: enter 2. Quit the game: Enter 3")
        choice: str = input("Enter one of the following numbers to continue: ")
    
        if 1 == choice:
            print(f"You have now entered the coin game{player}. Your goal is to guess wheater the coin will land heads (1) or tails (2). To win, you need to guess right three times in a row.")
            print("one correct answer Will give you five points. If you win the game, you will gain 15 points. However, if you Guessed incorrectly you will lose or your points. Good luck!")
            a: int = 0
            
            while a < 4:
                guess: str = input("enter your guess")

                if randint(1, 2) == guess:
                    print("you guessed correct")
                    points = points + 5
                    a = a + 1
               
                else:
                    print("you guessed incorrectly. Try again")
                points = a * (-5)
                a = 0
        else:
            if 2 == choice:
                print(f"You have now entered the math game{player}. In this Game, you will encounter several math questions. Good luck!")
                qop: str = input("if you want to play one round of the game, enter 1. If you want to go back to lobby, Enter 2")

                while 1 == int(qop):
                    n_1: str = input("enter your first number: ")
                    n_2: str = input("enter your Second number: ")
                    answer: str = input("what is your Answer? ")

                    if answer == math(int(n_1), int(n_2)):
                        print(f"{player}, you guessed correctly. You answered{answer}  and  the correct answer was{math(int(n_1), int(n_2))}")
                        qop: str = input("if you want to play one round of the game, enter 1. If you want to go back to lobby, Enter 2")
                        points = points + 5
                    else:
                        print(f"your guessed incorrectly.You answered{answer}  and  the correct answer was{math(int(n_1), int(n_2))}")
                        qop: str = input("if you want to play one round of the game, enter 1. If you want to go back to lobby, Enter 2")
            else:
                i = 0
        

if __name__ == "__main__":
    main()