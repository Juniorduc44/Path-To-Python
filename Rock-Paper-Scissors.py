#"answer" & "answer2" will equal what ever input is entered by the player. r/p/s is stated as the only choices.
answer = input("Player 1 (r/p/s): ")
answer2 = input("Player 2 (r/p/s: ")

#This "if" function will be activated if "r" is entered by player.
#if "r" is entered by the first player, then it falls into a nest
#of options limited to either "s" or "p". If "r" is chosen again
#it will print an error on screen that says "Sorry..."
#otherwise if an invalid character is entered the "else" parameter
#will become active and different error will show that says "...Try again."
#This full nest of "if" functions all act the same just for a different
#order of the chosen characters. Which creates a simple enough basket of
#functions which is Rock Paper Scissors.
if answer == "r":
if answer2 == "s":
print("Player 1 wins! Rock Beats Scissors!!")
elif answer2 == "p":
print("Player 2 Wins!! Paper beats Rock!!")
elif answer2 == "r":
print("Sorry Rock and Rock. Its a tie. Try again.")
else:
print("incorrect input registered. Try again.")
elif answer == "s":
if answer2 == "p":
print("Player 1 wins! Paper beats rock!!")
elif answer2 == "r":
print("Player 2 Wins!! Rock beats Scissors!!")
elif answer2 == "s":
print("Sorry Scissors and Scissors. Its a tie. Try again.")
else:
print("incorrect input registered. Try again.")
elif answer == "p":
if answer2 == "r":
print("Player 1 Wins!! Paper beats Rock!!")
elif answer2 == "s":
print("Player 2 Wins!! Scissors beats Paper!!")
elif answer2 == "p":
print("Sorry Paper and Paper. Its a tie. Try again.")
else:
print("incorrect input registered. Try again.")
