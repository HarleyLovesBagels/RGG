# Random Number guessing game

# Create a rnadom number betwenen 1 - 100
import random

randNum = random.randint(1,100)

score = 0

guess = 0
# receive user input guess
    
# if correct winner and print statement
def ansCheck(inp, ans):
  if (inp < 1 or inp > 100) :
    print('Not valid')
  elif ans > inp :
    print('Higher')
  elif ans < inp:
    print('Lower')
  else:
      print('Correct')
      print(f"Guesses : {score}")
      raise SystemExit
      
# if higher or lower retry
    

while guess != randNum:
  
  valid = False
  while not valid:
      try:
         guess = int(input('Enter a guess number from 1 - 100 : '))
         ansCheck(guess, randNum)
         score += 1
         if guess == int:
             valid = True
             guess = int(input('Enter a guess number from 1 - 100 : '))
      except ValueError:
             print("Not Valid")
    

# record number of tries

