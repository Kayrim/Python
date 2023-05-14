import random

def getChoices():
    player_choice = input("Enter your choice: ")
    computer_choice = random.choice(["rock", "paper", "scissors"])

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices

def determineWinner(choices):
    player_choice = choices["player"]
    computer_choice = choices["computer"]

    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "PAPER COVERS ROCK"
        elif computer_choice == "scissors":
            return "You destroyed the scissors with your rock"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player"
    else:
        return "computer"

def main():
    choices = getChoices()
    winner = determineWinner(choices)

    print("Player chose: " + choices["player"])
    print("Computer chose: " + choices["computer"])

    if winner == "tie":
        print("It's a tie!")
    else:
        print(winner + " wins!")

main()

# Stopped video at 35:12  https://youtu.be/eWRfhZUzrAc?t=2112