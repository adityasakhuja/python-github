import random
import math
from words import word_list
import pygame
from pygame.locals import (KEYDOWN, K_ESCAPE)

# Global Constants
WIDTH = 1000
HEIGHT = 600
BACKGROUND = pygame.Color("#031634")
LINE_COLOUR = pygame.Color("#E8DDCB")
MAN_COLOUR = pygame.Color("#CDB380")
GUESSES_LEFT = 6

# Get word from list
def get_word():
	word = random.choice(word_list)
	return word.upper()

def playGUI(word):
	# Pygame Initialisation
	pygame.init()
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Don't Hang the Man")
	headingFont = pygame.font.Font("kindergarten-hands.ttf", 80)
	textFont = pygame.font.SysFont(None, 28)
	attemptFont = pygame.font.SysFont(None, 50)

	# Heading
	heading = headingFont.render("Don't Hang the Man!", True, MAN_COLOUR)
	headingRect = heading.get_rect()
	headingRect.centerx = screen.get_rect().centerx
	headingRect.centery = 75

	# Instructions
	instructions1 = textFont.render("Don't let the man hang!", True, MAN_COLOUR)
	instructions1Rect = instructions1.get_rect()
	instructions1Rect.x = 600
	instructions1Rect.y = 200

	instructions2 = textFont.render("Guesses Left:", True, MAN_COLOUR)
	instructions2Rect = instructions2.get_rect()
	instructions2Rect.x = 600
	instructions2Rect.y = 250

	# Variables
	attempt = "_ " * len(word)
	guessed = False
	guessed_letters = []

	# Main Loop
	while not guessed:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					guessed = True

		# Static Elements
		screen.fill((BACKGROUND))
		screen.blit(heading,headingRect)
		screen.blit(instructions1, instructions1Rect)
		screen.blit(instructions2, instructions2Rect)

		# Guesses Left Score
		guessesLeft = textFont.render(str(GUESSES_LEFT), True, MAN_COLOUR)
		guessesLeftRect = guessesLeft.get_rect()
		guessesLeftRect.x = 740
		guessesLeftRect.y = 250
		screen.blit(guessesLeft, guessesLeftRect)

		attemptDisplay = attemptFont.render(attempt, True, MAN_COLOUR)
		attemptDisplayRect = attemptDisplay.get_rect()
		attemptDisplayRect.centerx = 700
		attemptDisplayRect.centery = 300
		screen.blit(attemptDisplay, attemptDisplayRect)

		# Surface flip
		pygame.display.flip()

playGUI("word")

# def drawHangmanGUI(GUESSES_LEFT):
# 	sixGuesses():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 	fiveGuesses():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 	fourGuesses():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 		# Torso
# 		pygame.draw.line(screen, MAN_COLOUR, (250,250), (250,450), 3)
# 	threeGuesses():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 		# Torso
# 		pygame.draw.line(screen, MAN_COLOUR, (250,250), (250,450), 3)
# 		# Left Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (180, 300), 3)
# 	twoGuesses():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 		# Torso
# 		pygame.draw.line(screen, MAN_COLOUR, (250,250), (250,450), 3)
# 		# Left Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (180, 300), 3)
# 		# Right Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (320, 300), 3)
# 	oneGuess():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 		# Torso
# 		pygame.draw.line(screen, MAN_COLOUR, (250,250), (250,450), 3)
# 		# Left Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (180, 300), 3)
# 		# Right Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (320, 300), 3)
# 		# Left Leg
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 450), (180, 475), 3)
# 	zeroGuess():
# 		# Base
# 		pygame.draw.line(screen, LINE_COLOUR, (100,550), (400,550), 3)
# 		# Pole
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (100,550), 3)
# 		# Top
# 		pygame.draw.line(screen, LINE_COLOUR, (100,150), (250,150), 3)
# 		# Head
# 		pygame.draw.circle(screen, MAN_COLOUR, (250,200), 50, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (225,190), 5, 0)
# 		pygame.draw.circle(screen, LINE_COLOUR, (275,190), 5, 0)
# 		pygame.draw.line(screen, LINE_COLOUR, (250,195), (250,205), 3)
# 		pygame.draw.circle(screen, LINE_COLOUR, (250, 230), 11, 3)
# 		# Torso
# 		pygame.draw.line(screen, MAN_COLOUR, (250,250), (250,450), 3)
# 		# Left Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (180, 300), 3)
# 		# Right Arm
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 325), (320, 300), 3)
# 		# Left Leg
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 450), (180, 475), 3)
# 		# Right Leg
# 		pygame.draw.line(screen, MAN_COLOUR, (250, 450), (320, 475), 3)

# 	switch = {
# 		6: sixGuesses()
# 		5: fiveGuesses()
# 		4: fourGuesses()
# 		3: threeGuesses()
# 		2: twoGuesses()
# 		1: oneGuess()
# 		0: zeroGuess()
# 	}





# def display_hangmanCLI(GUESSES_LEFT):
# 	stages = [
# 	# Sixth Mistake: Head + Torso + Both Arms + Both Legs
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|       \\|/
# 	|        |
# 	|       /|\\
# 	--
# 	""",
# 	# Fifth Mistake: Head + Torso + Both Arms + Left Leg
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|       \\|/
# 	|        |
# 	|       /|
# 	--
# 	""",
# 	# Fourth Mistake: Head + Torso + Both Arms
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|       \\|/
# 	|        |
# 	|        |
# 	--
# 	""",
# 	# Third Mistake: Head + Torso + Left Arm
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|       \\|
# 	|        |
# 	|        |
# 	--
# 	""",
# 	# Second Mistake: Head + Torso
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|        |
# 	|        |
# 	|        |
# 	--
# 	""",
# 	# First Mistake: Head
# 	"""
# 	----------
# 	|        |
# 	|        o
# 	|
# 	|
# 	|
# 	--
# 	""",
# 	# Initial Stage: No Hangman
# 	"""
# 	----------
# 	|        |
# 	|
# 	|
# 	|
# 	|
# 	--
# 	"""
# 	]
# 	return stages[tries]

# def playCLI(word):
# 	# Setup and Variables
# 	attempt = "_" * len(word)
# 	guessed = False
# 	guessed_letters = []
# 	guessed_words = []
# 	tries = 6

# 	# Instructions
# 	print("Let's play Hangman!")
# 	print("A simple command line game of Hangman")
# 	print("Check for letters or guess the word")
# 	print("You have 6 guesses! Let's get guessing!")
# 	print(display_hangman(6))
# 	print(attempt)
# 	print("\n")

# 	# Game Logic
# 	while not guessed and GUESSES_LEFT > 0:
# 		guess = input("Please guess a letter or word: ").upper()
# 		if len(guess) == 1 and guess.isalpha():
# 			if guess in guessed_letters:
# 				print("You have already guessed the letter " + guess + ".")
# 			elif guess not in word:
# 				print("Oops! " + guess + " is not in the word.")
# 				GUESSES_LEFT -= 1
# 				guessed_letters.append(guess)
# 			else:
# 				print("Well done! " + guess + " is in the word.")
# 				guessed_letters.append(guess)
# 				list_of_letters = list(attempt)
# 				indices = [i for i, letter in enumerate(word) if letter == guess]
# 				for index in indices:
# 					list_of_letters[index] = guess
# 				attempt = "".join(list_of_letters)
# 				if "_" not in attempt:
# 					guessed = True
# 		elif len(guess) == len(word) and guess.isalpha():
# 			if guess in guessed_words:
# 				print("You have already guessed the word " + guess + ".")
# 			elif guess != word:
# 				print("Oops! " + guess + " is not the word.")
# 				GUESSES_LEFT -= 1
# 				guessed_words.append(guess)
# 			else:
# 				guessed = True
# 				attempt = word
# 		else:
# 			print("Not a valid guess!")

# 		print(display_hangman(GUESSES_LEFT))
# 		print(attempt)
# 		print("\n")
# 	if guessed:
# 		print("Congratulations, you guessed the word! You win!")
# 	else:
# 		print("Sorry, you ran out of guesses. The word was " + word + ". Better luck next time!")

# Main Function to drive game
# def main():

# 	word = get_word()
# 	play(word)
# 	while input("Play again? (Y/N) ").upper() == "Y":
# 		word = get_word()
# 		play(word)

# if __name__ == "__main__":
# 	main()