import random

def comuguess(x):
	upp=x
	low=1
	clues=' '
	while clues!="c":
		guessNumber=random.randint(low,upp)
		clues=input(f'the {guessNumber} if too highi (H) , if too low (L), if correct (C) : \n').lower()
		if clues=="h":
			upp=guessNumber-1
		elif clues=="l":
			low=guessNumber+1
	print(f'yaa yaa {guessNumber} is corect computer won the game')



comuguess(500)