import random
from words import word_list

def get_word():
	word = random.choice(word_list)
	return word.upper()

def display_hangman(tries):
	stages = [
	# Sixth Mistake: Head + Torso + Both Arms + Both Legs
	"""
	----------
	|        |
	|        o
	|       \\|/
	|        |
	|       /|\\
	--
	""",
	# Fifth Mistake: Head + Torso + Both Arms + Left Leg
	"""
	----------
	|        |
	|        o
	|       \\|/
	|        |
	|       /|
	--
	""",
	# Fourth Mistake: Head + Torso + Both Arms
	"""
	----------
	|        |
	|        o
	|       \\|/
	|        |
	|        |
	--
	""",
	# Third Mistake: Head + Torso + Left Arm
	"""
	----------
	|        |
	|        o
	|       \\|
	|        |
	|        |
	--
	""",
	# Second Mistake: Head + Torso
	"""
	----------
	|        |
	|        o
	|        |
	|        |
	|        |
	--
	""",
	# First Mistake: Head
	"""
	----------
	|        |
	|        o
	|
	|
	|
	--
	""",
	# Initial Stage: No Hangman
	"""
	----------
	|        |
	|
	|
	|
	|
	--
	"""
	]
	return stages[tries]

def play(word):
	# Setup and Variables
	attempt = "_" * len(word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 6

	# Instructions
	print("Let's play Hangman!")
	print("A simple command line game of Hangman")
	print("Check for letters or guess the word")
	print("You have 6 guesses! Let's get guessing!")
	print(display_hangman(6))
	print(attempt)
	print("\n")

	# Game Logic
	while not guessed and tries > 0:
		guess = input("Please guess a letter or word: ").upper()
		if len(guess) == 1 and guess.isalpha():
			if guess in guessed_letters:
				print("You have already guessed the letter " + guess + ".")
			elif guess not in word:
				print("Oops! " + guess + " is not in the word.")
				tries -= 1
				guessed_letters.append(guess)
			else:
				print("Well done! " + guess + " is in the word.")
				guessed_letters.append(guess)
				list_of_letters = list(attempt)
				indices = [i for i, letter in enumerate(word) if letter == guess]
				for index in indices:
					list_of_letters[index] = guess
				attempt = "".join(list_of_letters)
				if "_" not in attempt:
					guessed = True
		elif len(guess) == len(word) and guess.isalpha():
			if guess in guessed_words:
				print("You have already guessed the word " + guess + ".")
			elif guess != word:
				print("Oops! " + guess + " is not the word.")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				attempt = word
		else:
			print("Not a valid guess!")

		print(display_hangman(tries))
		print(attempt)
		print("\n")
	if guessed:
		print("Congratulations, you guessed the word! You win!")
	else:
		print("Sorry, you ran out of tries. The word was " + word + ". Better luck next time!")


# Main Function to drive game
def main():
	word = get_word()
	play(word)
	while input("Play again? (Y/N) ").upper() == "Y":
		word = get_word()
		play(word)

if __name__ == "__main__":
	main()









