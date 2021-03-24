# Import packages to extend Python (just like we extend sublime, atom or VSCode)
from random import randint

# [] ==> this is an array
# name = [value1, value 2]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at zero

choices = ["rock", "paper","scissors"]

# Version 1, to explain array indexing
# player_choice = choices[1]
# print("index 1 in the choice array is " + player_choice + ", which is paper")

player_choice = input("choose rock , paper , or scissors: ")

print("user chose " + player_choice)

# this will be the AI choice -> a random pick frmo the choices array
computer_choice = choices[randint(0, 2)]

print ("computer_choice: " + computer_choice)