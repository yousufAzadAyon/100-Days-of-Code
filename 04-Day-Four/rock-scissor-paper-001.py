import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choice = int(input('what do you chose?\npress 0 for Rock, 1 for Paper, and 2 for Scissors\n:'))
random_choice = random.randint(0,2)

print(f'Your choice {game_images[choice]}\ncomputer choice{game_images[random_choice]}')

if choice == random_choice:
    print('Its a tie!')

if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and random_choice == 2:
  print("You win!")
elif random_choice == 0 and choice == 2:
  print("You lose")
elif random_choice > choice:
  print("You lose")
elif choice > random_choice:
  print("You win!")
elif random_choice == choice:
  print("It's a draw")