import random
moves = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0
while True:
    computer = random.choice(moves)
    player = input("Rock, Paper, Scissors ?")
    if player == computer:
        print("Tie !")
    elif player == "Rock":
        if computer == "Paper":
            print("Lose, Paper covers you")
            cpu_score = cpu_score + 1
        else:
            print("Win, You beat scissors")
            player_score = player_score + 1
    elif player == "Paper":
        if computer == "Rock":
            print("Win, you cover Rock")
            player_score = player_score + 1
        else:
            print("Lose, Scissors cut you")
            cpu_score = cpu_score + 1
    elif player == "Scissors":
        if computer == "Paper":
            print("Win, You cut Paper ")
            player_score = player_score + 1
        else:
            print("Lose, Rock beat  you")
            cpu_score = cpu_score + 1
    elif player == "End":
        print("Final Score: ")
        print("Player Score: ",player_score)
        print("Cpu Score: ", cpu_score)
        break