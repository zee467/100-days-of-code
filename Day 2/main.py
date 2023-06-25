import random

# Welcome message
print("Welcome to the Band Name Generator.")

# Ask user for city name
city = input("Which city did you grow up in?\n")

# Ask user for pet name
pet_name = input("What's your pet's name?\n")

# Band name generated
random_num = random.randint(1, 10)
print(f"Your band name could be {city} {pet_name}{random_num}")
