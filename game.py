from random import randint

choices = ["rock", "paper","scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

player_choice = False 

def winorlose(status):
	print("")
	print("\033[1;31m Keanu Reeves has spoken:\033[m \033[7;31m YOU \033[m", status, "! Do you want a rematch?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("\033[32m You chose to quit. Hope to see you soon!\033[m")
		print("")
		exit()
	elif choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("\033[31m Make a valid choice: Would you like to play again? Y for yes or N for no \033[m")
		choice = input("Y / N? ")

while player_choice is False:
	print("")
	print("\033[1;35m ~~~~~~~~~~~~~~~~~~~~~~|\033[m \033[7;35m  RPS GAME \033[m \033[1;35m|~~~~~~~~~~~~~~~~~~~~~~\033[m")
	print("  Matrix lives:", computer_lives, "/", total_lives)
	print("  Your lives:", player_lives, "/", total_lives)
	print("\033[1;35m  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
	print("")
	print("\033[1m Choose your weapon! \033[m If you want to leave, type quit to exit.")

	player_choice = input("rock, paper, or scissors?  ")

	if player_choice == "quit" or player_choice == "Quit":
		print("You chose to \033[1m quit.\033[m Hope to see you soon!")
		print("")
		exit()

	print("")
	print("\033[36m You chose \033[m" + player_choice)

	computer_choice = choices[randint(0, 2)]

	print ("\033[34m The Matrix chose \033[m" + computer_choice)
	print ("")

	if computer_choice == player_choice: 
		print ("\033[31m What a coincidence, it's a tie!\033[m")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("\033[31m Oh no, you got broken! \033[m")
			player_lives -= 1
		else:
			print("\033[31m You're a nice wrap. Well played! \033[m")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("\033[31m That's a nice cut! Well done.\033[m")
			computer_lives -= 1
		else:
			print("\033[31m You lost by being the lamest christmas gift... \033[m")
			player_lives -= 1

	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("\033[31m You lost! At least you can be a wonderful origami now.\033[m")
			player_lives -= 1
		else:
			print("\033[31m Wow, you ROCK! Nicely done.\033[m")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("\033[7;31m LOSE \033[m")

	if computer_lives == 0:
		winorlose("\033[7;31m WON \033[m")
	
	print("")
	print("\033[37m ~~| Lives bord |~~\033[m ")	
	print("\033[37m Your lives: \033[m ", player_lives)
	print("\033[37m Matrix lives: \033[m ", computer_lives) 

	player_choice = False


