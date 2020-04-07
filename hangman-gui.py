import random
from words import word_list
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hangman")

# Global Variables & Constants
GUESSES = 6
baseCoord = 20, 200, 200, 200
poleCoord = 20, 205, 20, 10
topCoord = 20, 12, 150, 12
cordCoord = 148, 10, 148, 30
headCoord = 133, 30, 163, 60
torsoCoord = 148, 60, 148, 150
leftHandCoord = 148, 105, 120, 80
rightHandCoord = 148, 105, 176, 80
leftLegCoord = 148, 150, 120, 170
rightLegCoord = 148, 150, 176, 170
heading = "Don't let the man Hang!"
INSTRUCTIONS = StringVar()
INSTRUCTIONS.set("You have " + str(GUESSES) + " chances left to save the man. Click the letters to guess.")

def get_word():
	word = random.choice(word_list)
	print(word)
	return word.upper()

WORD = get_word()
ATTEMPT = StringVar()
ATTEMPT.set("-" * len(WORD))
GUESSED = False
GUESSED_LETTERS = []

print(GUESSES)


hangman = Canvas(root)

def createLabel(variable, text, fontsize, row, ypadding, xpadding):
	if variable:
		Label(root, textvariable=text, font=("Helvetica", fontsize)).grid(row=row, columnspan=14, sticky="N", pady=ypadding, padx=xpadding)
	else:
		Label(root, text=text, font=("Helvetica", fontsize)).grid(row=row, columnspan=14, sticky="N", pady=ypadding, padx=xpadding)

def createButton(text, row, col):
	Button(root, text=text, bd=0, padx=10, pady=5, command=lambda:checkLetter(text)).grid(row=row, column=col)

def createInputButtons():
	alphabet = []
	alpha = 'a'
	for i in range(0, 26): 
		alphabet.append(alpha) 
		alpha = chr(ord(alpha) + 1)
	i = 0
	while i < 26:
		if i < 13:
			row = 5
			col = i + 2
		else:
			row  = 6
			col = i - 11
		createButton(alphabet[i].upper(), row, col)
		i += 1

# Hangman States
def hangmanSix():
	base = hangman.create_line(baseCoord, width=10)
	pole = hangman.create_line(poleCoord, width=10)
	top = hangman.create_line(topCoord, width=5)
	cord = hangman.create_line(cordCoord, width=5)
def hangmanFive():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	head = hangman.create_oval(headCoord, width=3)
def hangmanFour():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	# head = hangman.create_oval(headCoord, width=3)
	torso = hangman.create_line(torsoCoord, width=3)
def hangmanThree():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	# head = hangman.create_oval(headCoord, width=3)
	# torso = hangman.create_line(torsoCoord, width=3)
	leftHand = hangman.create_line(leftHandCoord, width=3)
def hangmanTwo():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	# head = hangman.create_oval(headCoord, width=3)
	# torso = hangman.create_line(torsoCoord, width=3)
	# leftHand = hangman.create_line(leftHandCoord, width=3)
	rightHand = hangman.create_line(rightHandCoord, width=3)
def hangmanOne():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	# head = hangman.create_oval(headCoord, width=3)
	# torso = hangman.create_line(torsoCoord, width=3)
	# leftHand = hangman.create_line(leftHandCoord, width=3)
	# rightHand = hangman.create_line(rightHandCoord, width=3)
	leftLeg = hangman.create_line(leftLegCoord, width=3)
def hangmanZero():
	# base = hangman.create_line(baseCoord, width=10)
	# pole = hangman.create_line(poleCoord, width=10)
	# top = hangman.create_line(topCoord, width=5)
	# cord = hangman.create_line(cordCoord, width=5)
	# head = hangman.create_oval(headCoord, width=3)
	# torso = hangman.create_line(torsoCoord, width=3)
	# leftHand = hangman.create_line(leftHandCoord, width=3)
	# rightHand = hangman.create_line(rightHandCoord, width=3)
	# leftLeg = hangman.create_line(leftLegCoord, width=3)
	rightLeg = hangman.create_line(rightLegCoord, width=3)

def hangmanState(guesses):
	if guesses == 6:
		hangmanSix()
	elif guesses == 5:
		hangmanFive()
	elif guesses == 4:
		hangmanFour()
	elif guesses == 3:
		hangmanThree()
	elif guesses == 2:
		hangmanTwo()
	elif guesses == 1:
		hangmanOne()
	elif guesses == 0:
		hangmanZero()
	hangman.grid(row=3, columnspan=14, pady=100)

def checkLetter(guess):
	print(guess)
	global GUESSES, GUESSED_LETTERS, ATTEMPT, INSTRUCTIONS, WORD, GUESSED
	if guess in GUESSED_LETTERS:
		print("already guessed ", WORD)
		INSTRUCTIONS.set("Oops! You've already guessed the letter " + guess + ". You have " + str(GUESSES) + " guesses left.")
	elif guess not in WORD:
		print("bad guess ", WORD)
		INSTRUCTIONS.set("Bad guessing! The poor man is about to be hanged. You have " + str(GUESSES) + " guesses left.")
		GUESSES -= 1
		hangmanState(GUESSES)
		GUESSED_LETTERS.append(guess)
	else:
		print("good guess ", WORD)
		INSTRUCTIONS.set("Well done! Keep on going to save the man!")
		GUESSED_LETTERS.append(guess)
		list_of_letters = list(ATTEMPT.get())
		print(list_of_letters)
		indices = [i for i, letter in enumerate(WORD) if letter == guess]
		for index in indices:
			list_of_letters[index] = guess
		ATTEMPT.set("".join(list_of_letters))
		print(ATTEMPT.get())
		if "-" not in ATTEMPT.get():
			print(GUESSED)
			GUESSED = True
			messagebox.showinfo("YOU WON", "Congratulations, you didn't let the man hang!")
			root.destroy()



# Main Logic
createInputButtons()
createLabel(False, heading, 26, 0, 20, 100)
createLabel(True, INSTRUCTIONS, 18, 1, 0, 100)
createLabel(True, ATTEMPT, 20, 2, 10, 100)
hangmanState(GUESSES)

# if GUESSED:
# 	print("detected guessed true")
	



root.mainloop()











