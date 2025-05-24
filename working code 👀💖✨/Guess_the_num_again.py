#💝 Guess the number:

guess = 0
tries = 0
while guess != 7 and tries < 5:
  guess = int(input('guess the number: ')) 
  tries = tries + 1
if guess != 7:
  print('you ran out of tries')
else:
  print('YOU GOT IT😁💗✨')