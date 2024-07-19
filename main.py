import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guessed_number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

while attempts > 0:
  print(f"You have {attempts} remaning to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == guessed_number:
    print("Congrats You Won!")
    break
  elif guess > guessed_number:
    print("Too HİGH!")
  else:
    print("Too LOW!")
  attempts -=1
if attempts == 0 and not guess == guessed_number:
  print("Your run out of attempts You Lose!")