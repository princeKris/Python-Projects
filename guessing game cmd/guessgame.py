import random

def guess(x):
	randomNumber=random.randint(1,x)
	guessNumber=0
	while guessNumber!=randomNumber:
		guessNumber=int(input(f'guess the number b/t (1,{x})'))
		if guessNumber>randomNumber:
			print(f'the {guessNumber} is greater than com guess number')
		elif guessNumber<randomNumber:
			print(f'the {guessNumber} is smaller than com guess number')
	print(f'yaa yaa you won the game')


guess(100)