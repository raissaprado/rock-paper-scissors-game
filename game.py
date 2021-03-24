from random import randint
	
choices = ["rock", "paper","scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

player_choice = False 

def winorlose(status):
	print("")
	print("Keanu Reeves has spoken: YOU", status, "! Do you want a rematch?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit. Hope to see you soon!")
		print("")
		exit()
	elif choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("Make a valid choice: Would you like to play again? Y for yes or N for no")
		choice = input("Y / N? ")

while player_choice is False:
	print("")
	print("~~~~~~~~~~~~~~~~~~~~~~| RPS GAME |~~~~~~~~~~~~~~~~~~~~~~")
	print("Matrix lives:", computer_lives, "/", total_lives)
	print("Your lives:", player_lives, "/", total_lives)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("")
	print("Choose your weapon! If you want to leave, type quit to exit.\n")

	player_choice = input("rock, paper, or scissors? \n")

	if player_choice == "quit" or player_choice == "Quit":
		print("You chose to quit. Hope to see you soon!")
		print("")
		exit()

	print("")
	print("You chose " + player_choice)

	computer_choice = choices[randint(0, 2)]

	print ("The Matrix chose " + computer_choice)

	if computer_choice == player_choice: 
		print ("What a coincidence, it's a tie!")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("Oh no, you got broken!")
			player_lives -= 1
		else:
			print("You're a nice wrap. Well played!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("That's a nice cut! Well done.")
			computer_lives -= 1
		else:
			print("You lost by the lamest christmas gift")
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
	
	print("")
	print("~~| Lives bord |~~")	
	print("Your lives: ", player_lives)
	print("Matrix lives: ", computer_lives)

	player_choice = False


