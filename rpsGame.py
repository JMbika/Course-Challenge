import random

#Score Count
userScore = 0
computerScore = 0

#Lives Count
userLife = 3
computerLife = 3

choices = ["r", "p", "s"]

userChoice = input("What do you pick (r)ock, (p)aper, (s)cissors?")

computerChoice = random.choice(choices)
print("Computer chose:", computerChoice)

#compare the choices
if len(userChoice) == 0:
            print("Invalid answer. Try again")

if userChoice[0].lower() == computerChoice:
    print("Tie!")
            
elif userChoice[0].lower() == "r" and  computerChoice == "s":
    print("Computer Loses")
    userScore += 1

elif userChoice[0].lower() == "s" and  computerChoice == "r":
    print("User Loses")
    computerScore += 1

elif userChoice[0].lower() == "p" and  computerChoice == "s":
    print("User Loses")
    computerScore += 1

elif userChoice[0].lower() == "s" and  computerChoice == "p":
    print("Computer Loses")
    userScore += 1

elif userChoice[0].lower() == "r" and  computerChoice == "p":
    print("User Loses")
    computerScore += 1
            
elif userChoice[0].lower() == "p" and  computerChoice == "r":
    print("Computer Loses")
    userScore += 1

else:
    print("Invalid Answer. Try again!")

print("User Wins: ", userScore)
print("Computer wins: ", computerScore)
