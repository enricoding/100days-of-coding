# Tag 009 – Dictionaries, Nesting and the Secret Auction
**Datum:** [03.06.2026]
**Dauer:** [1,5 Stunden]

---

## Was ich heute gelernt habe
Wie ein Dictionarie funktioniert und wie man eine Liste in einer Liste hat und aus den Liste gezielt Sachen auslesen kann 

---

## Code des Tages
from art import logo
print(logo)
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

## Was war schwierig?

Mir viel es besonders schwer bei dem Projekt einen Anfang zu finden deswegen habe ich es Schritt für Schritt anch dem Video absolviert und dannach mein Verständnis vertieft.
---

## Meine eigene Abwandlung



## Morgen lerne ich

- [ ] Tag 10: Functions with Outputs
