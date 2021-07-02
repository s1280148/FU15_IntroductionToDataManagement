import random

userName = input("What is your name?\n")
print(f"Hello, {userName}!")

print("Rolling the dice...")

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(f"Die1 : {dice1}")
print(f"Die2 : {dice2}")

print(f"Total value : {dice1 + dice2}")

if dice1 + dice2 > 7 :
    print(f"{userName} won!")
else :
    print(f"{userName} lost.")