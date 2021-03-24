# Import packages to extend Python (just like we extend sublime, atom or VSCode)
from random import randint

# [] ==> this is an array
# name = [value1, value 2]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at zero
choices = ["rock", "paper","scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

# True or false are boolean data types
# essentially, booleand are equivalent to an on or off switch, 1 or 0.
player_choice = False 

#define a win or lose function
def winorlose(status):
	# version 1 of function
	# print("inside winorlose function; status is: ", status)
	print("Keanu Reeves has spoken: YOU", status, "! Do you want a rematch?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit. Hope to see you soon!")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		# and reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("Make a valid choice: Would you like to play again? Y for yes or N for No")
		# this might generate a bug that we need to fix later
		choice = input("Y / N? ")


#player_choice == False
while player_choice is False:
	print("")
	print("~~~~~~~~~~~~~~~~~~~~~~~~RPS GAME~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Matrix lives:", computer_lives, "/", total_lives)
	print("Your lives:", player_lives, "/", total_lives)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("")
	# Version 1, to explain array indexing
	# player_choice = choices[1]
	# print("index 1 in the choice array is " + player_choice + ", which is paper")

	player_choice = input("Choose your weapon: rock, paper, or scissors --> ")
	#player_choice now equals TRUE -> It has a value

	print("You chose " + player_choice)

	# this will be the AI choice -> a random pick from the choices array
	computer_choice = choices[randint(0, 2)]

	print ("The Matrix chose " + computer_choice)

	if computer_choice == player_choice: 
		print ("What a mind reader, it's a tie!")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("Oh no, you got broken!")
			#verbose way
			#player_lives = player_lives - 1
			#simplified way
			player_lives -= 1
		else:
			print("You're a nice wrap. Well played!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("That's a nice cut! Well done.")
			computer_lives -= 1
		else:
			print("You lost (or became the lamest christmas gift)")
			player_lives -= 1


	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("You lost! At least you can be a wonderful origami now.")
			player_lives -= 1
		else:
			print("Wow, you ROCK! Nicely done.")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("LOSE")

	if computer_lives == 0:
		winorlose("WON")
		
	print("Player lives: ", player_lives)
	print("Computer lives: ", computer_lives)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	player_choice = False


