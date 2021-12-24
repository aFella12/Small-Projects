import random

playerScore = 0
opponentScore = 0

playerMove = ""

opponent_moves = ["rock", "paper", "scissors"]

while playerMove != "quit":
    playerMove = input("Enter move: ")
    if (playerMove.lower() == "scissors") or (playerMove.lower() == "rock") or (playerMove.lower() == "paper"):
        opponent_num = random.randint(0, 2)
        opponentMove = opponent_moves[opponent_num]
        if (playerMove.lower() == "rock" and opponentMove == "rock"):
            print("Draw")
        elif (playerMove.lower() == "rock" and opponentMove == "paper"):
            print("You lost")
            opponentScore += 1
        elif (playerMove.lower() == "rock" and opponentMove == "scissors"):
            print("You won!")
            playerScore += 1
        elif (playerMove.lower() == "paper" and opponentMove == "rock"):
            print("You won!")
            playerScore += 1
        elif (playerMove.lower() == "paper" and opponentMove == "paper"):
            print("Draw")
        elif (playerMove.lower() == "paper" and opponentMove == "scissors"):
            print("You lost")
            opponentScore += 1
        elif (playerMove.lower() == "scissors" and opponentMove == "rock"):
            print("You lost")
            opponentScore += 1
        elif (playerMove.lower() == "scissors" and opponentMove == "paper"):
            print("You won!")
            playerScore += 1
        elif (playerMove.lower() == "scissors" and opponentMove == "scissors"):
            print("Draw")
    elif playerMove == "quit":
        print("GG")
    else:
        print("Invalid move, try again")
        continue
    opponent_num = random.randint(0, 2)
    opponentMove = opponent_moves[opponent_num]

if playerScore == opponentScore:
    print("Game Result: Draw")
elif playerScore < opponentScore:
    print("Game Result: You Lost")
elif playerScore > opponentScore:
    print("Game Result: You Won!!!\nCongrats!!!")


