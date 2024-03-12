import random

def roll_dice(num_dice, num_sides):
    print("Rolling the dice...")
    for i in range(num_dice):
        print(f"Die {i + 1}: {random.randint(1, num_sides)}")

num_dice = int(input("Enter the number of dice: "))
num_sides = int(input("Enter the number of sides on each die: "))

roll_dice(num_dice, num_sides)