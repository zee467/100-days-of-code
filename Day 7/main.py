from ascii import logo, stages
from hangman_words import word_list
import random

lives = 6

# Display the logo
print(logo)

# Randomly chose a word from word_list
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]

letters_guessed = []
while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess.isalpha():
        if len(guess) == 1:
            if guess in letters_guessed:
                print(f"You've already guessed {guess}\n")
            else:
                if guess in chosen_word:
                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guess:
                            display[i] = guess
                            
                    if "_" not in display:
                        print("You win.")
                else:
                    lives -= 1
                    print(f"You guessed {guess}, that's not in the word. You lose a life.")
                    if lives == 0:
                        print("You lose.")
                        print(f"The answer was {chosen_word}")
                
                letters_guessed.append(guess)
                print("".join(display))
                print(stages[lives])
        else:
            print("You ought to enter one letter\n")
            continue
    else:
        print("You didn't enter any alphabet.\n")
        continue

