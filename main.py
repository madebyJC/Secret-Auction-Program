from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

bid = {}
bidding = True
def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The highest bid is {winner} with a bid of ${highest_bid}.")

while bidding == True:
  
  name_input = input("What is your name? ")
  bid_input = int(input("What is your bid? $" ))
  
  name = name_input
  bid[name] = bid_input

  user_continue = input("Are there any other bidders? Type \"yes\" or \"no\"\n").lower()
  if user_continue == "yes":
    clear()
    print(logo + "\n")
  elif user_continue == "no":
    bidding = False
    highest_bidder(bidding_record=bid)







  