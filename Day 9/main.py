from art import logo


# An auction program

print(logo)
print("Welcome to the secret auction program.")

bid_info = {}
ask_again = True


def find_highest_bidder(bid_details):
    highest = 0
    winner = None
    for key, value in bid_details.items():
        if value > highest:
            highest = value
            winner = key

    return highest, winner


while ask_again:
    bidder_name = input("What is your name?: ").strip().capitalize()
    bid_amount = int(input("What's your bid?: $"))
    bid_info[bidder_name] = bid_amount

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()

    if other_bidders == "yes":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif other_bidders == "no":
        ask_again = False

        highest_val, highest_bidder = find_highest_bidder(bid_info)

        print(f"The winner is {highest_bidder} with a bid of ${highest_val}.")

