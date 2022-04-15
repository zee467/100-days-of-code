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

image = [rock, paper, scissors]

user_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_value < 0 or user_value > 2:
    print("You typed an invalid number. You lose.")
else:
    print(image[user_value])
    computer_value = random.randint(0, 2)
    print(f"Computer chose: \n{image[computer_value]}")
    if user_value == 1 and computer_value == 0:
        print("You win")
    elif user_value == 0 and computer_value == 2:
        print("You win!")
    elif user_value == 2 and computer_value == 1:
        print("You win!")
    elif user_value == computer_value:
        print("Draw")
    else:
        print("Computer wins!")