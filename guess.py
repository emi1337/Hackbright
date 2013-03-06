from random import randint

def inputValidation(input):
	while input == '':
		print "Sorry, I didn't catch that. Try again."
		input = raw_input("> ")
	input = int(input)
	while (input < 1) or (input > 100):
		print "Hey, that wasn't between 1 and 100, silly! Try again."
		input = inputValidation(raw_input("> "))
	return input

def playGame():
	print "Hi there! What is your name?"
	name = raw_input("> ")
	number = randint(1,100)
	print "Alrighty, %s, I'm thinking of a number between 1 and 100." % name
	print "What's your guess? "
	player_guess = inputValidation(raw_input("> "))
	
	
	while player_guess != number:
		if (player_guess < number):
			print "Too low."
		else:
			print "Too high."
		player_guess = inputValidation(raw_input("Try again. \n> "))

	print "Good job! You got it right! The number was %d." % number 

	play_again = raw_input("Would you like to reset the game? Type 'Yes' or 'No'. > ")
	if play_again.lower() == "yes":
		playGame()
	elif play_again.lower() == "no":
		print "Aww, okay. Bye then!"
	else:
		print "I'm sorry, I'm not sure what you wanted. Could you type 'Yes' or 'No'?"

playGame()
