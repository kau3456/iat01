import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for i in range(num_dice)]
    return results

def func():
    while True:
        print("Welcome to the Dice Roller App!")
        num_dice = int(input("Enter the number of dice you want to roll: "))

        if num_dice <= 0:
            print("Please enter a valid number of dice.")
            continue

        results = roll_dice(num_dice)
        print(f"Result: {', '.join(map(str, results))}")

        play_again = input("Roll the dice again? (yes/no): ")
        if play_again != "yes":
            print("Thanks for using the Dice Roller App!")
            break
        
func()



