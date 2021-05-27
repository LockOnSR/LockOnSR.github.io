import time
import random
min = 1
max = 6

coins = 100

print("Welcome to The Casino!")
time.sleep(1)
print("The name of the game here is DICE")
time.sleep(1)
print("Beat The Casino and win some Coins!")
time.sleep(1)
print("If you lose all your your Coins we will throw you out!")
()
()
time.sleep(1)
dice = input("Want to play a round of DICE?(Y/N): ")

while dice == "Y" or dice == "y":
    print("Rolling the dice...")
    time.sleep(1)
    print("You rolled...")
    time.sleep(1)
    total = random.randint(min, max) + random.randint(min, max)
    time.sleep(1)
    print("The Casino rolled...")
    time.sleep(1)
    casinoTotal = random.randint(min, max) + random.randint(min, max)

    if (casinoTotal > total):
        results = "Lost!"
        coins = coins-25
    elif (casinoTotal < total):
        results = "Won!"
        coins = coins+50
    else:
        results = "Was a Draw! What are the odds!"

    print ("Your roll of", total, "against the Casino's roll of", casinoTotal, results)
    time.sleep(1)
    print ("Your current Coins value is: ", coins)
    time.sleep(1)

    if coins == 0:
        print("You're out of coins")
        print("Come back when you get some more!")
        quit
    elif coins == 1000:
        print("You're playing this too much")
        print("You'll make the casino go broke!")
        quit
    else:
        dice = input("Play another round?(Y/N) ")

if dice == "n" or dice == "N":
    print("Thanks for Stopping by The Casino!")
    ()
    time.sleep(1)
    print("We hope to see you again real soon!")
    time.sleep(2)
    quit
