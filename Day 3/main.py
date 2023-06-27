from ascii import ascii_art

print(ascii_art)

# Welcome message
print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if direction == "right":
  print("You fell into a hole. Game Over.")
elif direction == "left":
  wait_or_swim = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()

  if wait_or_swim == "swim":
    print("You get attacked by an angry trout. Game Over.")
  elif wait_or_swim == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n").lower()
    
    if door == "yellow":
      print("You found the treasure! You Win!")
    elif door == "blue":
      print("You enter a room of beasts. Game Over.")
    elif door == "red":
      print("It's a room full of fire. Game Over.")
else:
  print("Invalid input")
      
