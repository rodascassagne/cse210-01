
import random
number = random.randint(1, 13)

name = input("Hello, what's your name?")

turns = 0

print( name + " you can choose cards between 1 and 13:")

while turns < 6:
    card = int(input("try a card between 1 and 13: "))
    turns = turns + 1
    if card < number:
        print("card is low")
    elif card > number:
        print("card is too high")
    else:
        break
if card == number:
    print("you won")
else:
   
    print(f"You lost, the card was : {number}")
    