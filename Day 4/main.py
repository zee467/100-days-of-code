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

# Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

game_option = [rock, paper, scissors]

computer_val = random.randint(0, 2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choice_matrix = [
  ["It's a draw", "You win!", "You lose"],
  ["You lose", "It's a draw", "You win!"],
  ["You win!", "You lose", "It's a draw"]
]

if user_choice not in [0, 1, 2]:
  print("Invalid choice. Game over!")
else:
  print(game_option[user_choice])
  print(f"Computer chose: \n{game_option[computer_val]}")
  print(choice_matrix[computer_val][user_choice])
  
  




  
  



