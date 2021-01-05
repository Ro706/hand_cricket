import random 
from pyfiglet import Figlet
f=Figlet(font ='slant')
print(f.renderText('hand_cricket'))

score = 0 
a=0


print("Lets Toss")
select_OorE = input("Select Odd or Even [O/E] ").lower()
#print(f"You chose {select_OorE}")
number_for_toss = int(input("Enter a number between 1-6 "))
computer_number = random.randint(1,6)
print(f"computer's number is {computer_number}")
total_for_toss = number_for_toss + computer_number
tosswon = total_for_toss % 2

if tosswon == 0:
  toss = "e"
else:
  toss = "o"

if toss == select_OorE:
  
  print("\nYou bat first...")
  while True:
    a = 1
    player = int(input("\nPlay your shot [1,2,3,4,5,6] "))
    computer_number = random.randint(1,6)
    if player == computer_number:
      print(f"Your Out... Your Score = {score}")
      print(f"computer tried to defend you with {computer_number}")
      break
    else:
      score += player
      print(f"computer tried to defend you with {computer_number}\n\nYour score = {score}")

else:
  
  print("You lost the toss.... So Computer will bat first")
  while True:
    player = int(input("Defend computer's shot [1,2,3,4,5,6] "))
    computer_number = random.randint(1,6)
    print(f"computer's shot {computer_number}")
    if player == computer_number:
      print(f"Computer is Out... It's Score = {score}")
      break
    else:
      score += computer_number
      print(f"Your shot is {player}...\n\nYour score = {score}")

target = score + 1 
print(f"TOTAL SCORE = {target}")
print("\n.....Second Innings.....")
computer_score = 0
player_score = 0

if a != 0:
  while True:
    player = int(input("Defend computer's shot [1,2,3,4,5,6] "))
    computer_number = random.randint(1,6)
    print(f"computer's shot{computer_number}")
    if player == computer_number:
      print(f"Computer is Out... It's Score = {computer_score}")
      break
    else:
      computer_score += computer_number
      print(f"Computer score = {computer_score}\n\nComputer still need {target - computer_score}") 
      if computer_score >= target:
        print(f"Sorry you lost...")
        break

else:
  while True:
    player = int(input("\nPlay your shot [1,2,3,4,5,6] "))
    computer_number = random.randint(1,6) 
    if player == computer_number:
      print(f"You lost by {target - player_score} runs.....\nTRY AGAIN")

    else:
      player_score += player
      print(f"Your score is {player_score}\n\nYou still need {target - player_score} runs to WIN")
      if player_score >= target:
        print("Congrats You won....")
        break



