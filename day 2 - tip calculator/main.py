print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_in_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
bill_with_tip = bill + ((tip_in_percentage / 100) * bill)
each_person = bill_with_tip / num_of_people
print(f"Each person should pay: ${each_person:.2f}")


