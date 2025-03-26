import random
cpSc = 0
pSc = 0
chances = 5
moves = [
    "rock",
    "paper",
    "scissors"
]
while chances > 0:
    cp = random.choice(moves)
    p = input("Enter rock, paper, or scissors. ")
    print(cp)
    print(p)
    if cp == p:
        print("It was a tie!")
    elif cp == "scissors" and p == "paper" or cp == "paper" and p == "rock" or cp == "rock" and p == "scissors":
        print("The computer wins!")
    elif p == "scissors" and cp == "paper" or p == "paper" and cp == "rock" or p == "rock" and cp == "scissors":
        print("You win!")
    else:
        print("Stop.")
        chances = 0
    chances -= 1

if cpSc > pSc:
    print("The computer wins overall!")
elif cpSc < pSc:
    print("You win overall!")
elif cpSc == pSc:
    print("Overall, it was a tie.")
