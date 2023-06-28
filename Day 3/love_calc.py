print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1 + name2).lower()

first_num = 0

# add the number of occurence of each letter in the name to first_num
for letter in "true":
    first_num += combined_name.count(letter)

second_num = 0
for letter in "love":
    second_num += combined_name.count(letter)

# converts the string to an int
score = int(str(first_num) + str(second_num))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together \
    like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

