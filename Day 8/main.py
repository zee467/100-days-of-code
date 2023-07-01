from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(plain_text, shift_number, cipher_direction):
    # changes the shift number to a negative value if the direction is decode
    if cipher_direction == "decode":
        shift_number *= -1

    new_text = ""
    for ch in plain_text:
        if ch not in alphabet:
            new_text += ch
        else:
            position = alphabet.index(ch)
            new_ch = alphabet[(position + shift_number) % 26]
            new_text += new_ch

    return new_text
  
go_again = True
while go_again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
  if direction != "encode" or direction != "decode":
     continue
  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Displays the result from the function
  result = caesar(text, shift, direction)
  print(f"Here is the {direction}d result: {result}")
 
  # The value determines if the loop will execute again
  user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
  if user_input == "no":
    go_again = False
    print("Goodbye.")
  elif user_input == "yes":
    go_again = True