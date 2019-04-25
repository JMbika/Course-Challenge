import random

choices = ["r", "p", "s"]

computerChoice = random.choice(choices)
print("Computer chose:", computerChoice)

userChoice = input("What do you pick (r)ock, (p)aper, (s)cissors?")
