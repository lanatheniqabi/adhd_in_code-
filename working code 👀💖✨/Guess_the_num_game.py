#💝 Guess the number game:

import random

secret_number = random.randint(1,10)
guess = None
turns = 0

while guess != secret_number:
    guess = int(input('guess a number darling: '))
turns += 1
if guess < secret_number:
    print('dang! too low😅')
elif guess > secret_number:
    print('Uhh ohh! you are too high🙃')
else:
    print(f'yes! you did it! in {turns} tries😍')
