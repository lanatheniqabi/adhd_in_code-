#💝 Sorting hat:

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
question = ('Q1) Do you like Dawn or Dusk? 1:dawn 2:dusk')
print (question)
answer = int(input('enter choice [1-2]: '))
if answer == 1:
  gryffindor += 1
  ravenclaw += 1
  print('+1 to Gryffindor and Ravenclaw')
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
  print('Hufflepuff and Slytherin both get +1')
else: 
  print('Wrong output!')
question = ('Q2) When I’m dead, I want people to remember me as: 1: The Good 2: The Great 3: The Wise 4: The Bold')
print(question)
answer = int(input('enter choice [1-4]: '))
if answer == 1:
  hufflepuff += 2
  print('Hufflepuff 2+')
elif answer == 2:
  slytherin += 2 
  print('Slytherin 2+')
elif answer == 3:
  ravenclaw += 2
  print('Ravenclaw 2+')
elif answer == 4:
  gryffindor += 2
  print('Gryffindor 2+')
else:
  print('Wrong output!') 
question = ('Q3) Which kind of instrument most pleases your ear?: 1: The violin 2: The trumpet 3: The piano 4: The drum')
print (question)
answer = int(input('enter choice [1-4]: '))
if answer == 1:
  slytherin += 4
  print('Slytherin +4')
elif answer == 2:
  hufflepuff += 4 
  print(' Hufflepuff +4')
elif answer == 3:
  ravenclaw += 4
  print('Ravenclaw +4')
elif answer == 4:
  gryffindor += 4
  print('Gryffindor +4')
else:
  print('Wrong output!')
print("\n Final House Scores:")
print("Gryffindor:", gryffindor)
print("Hufflepuff:", hufflepuff)
print("Ravenclaw:", ravenclaw)
print("Slytherin:", slytherin)
