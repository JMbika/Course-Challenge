import random

#Score Count
userScore = 0
computerScore = 0

#Lives Count
userLife = 3
computerLife = 3
choices = ["r", "p", "s"]
rnd = 1


while True:
    print("Round: ", rnd)
    userChoice = input("What do you pick (r)ock, (p)aper, (s)cissors?")
    computerChoice = random.choice(choices)
    print("Computer chose:", computerChoice)

    if len(userChoice) == 0:
        print("Invalid answer. Try again")

    if userChoice[0].lower() == computerChoice:
        print("Tie!")
                
    elif userChoice[0].lower() == "r" and  computerChoice == "s":
        print("Computer Loses")
        userScore += 1
        computerLife -= 1
        if computerLife == 0:
            break

    elif userChoice[0].lower() == "s" and  computerChoice == "r":
        print("User Loses")
        computerScore += 1
        userLife -= 1
        if userLife == 0:
            break

    elif userChoice[0].lower() == "p" and  computerChoice == "s":
        print("User Loses")
        computerScore += 1
        userLife -= 1
        if userLife == 0:
            break

    elif userChoice[0].lower() == "s" and  computerChoice == "p":
        print("Computer Loses")
        userScore += 1
        computerLife -= 1
        if computerLife == 0:
            break

    elif userChoice[0].lower() == "r" and  computerChoice == "p":
        print("User Loses")
        computerScore += 1
        userLife -= 1
        if userLife == 0:
            break
                
    elif userChoice[0].lower() == "p" and  computerChoice == "r":
        print("Computer Loses")
        userScore += 1
        computerLife -= 1
        if computerLife == 0:
            break

    else:
        print("Invalid Answer. Try again!")

    rnd = rnd + 1
    if rnd == 4:
        break

print("User Wins: ", userScore)
print("Computer wins: ", computerScore)
if userScore > computerScore:
    print("The User wins the game!")
elif computerScore > userScore:
    print("The Computer wins the game!")
else:
    print("It's a tie!")
