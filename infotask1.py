import random

print("Welcome to the Number Guessing Game!")
player_name = input("Please enter your name: ")
print("Hello, ",player_name,",! I'm thinking of a number between 1 and 100.")
    
while True:
    random_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
            n = int(input("Take a guess: "))
            if n<0 or n>100:
                print("Please enter a valid number.")
                continue
            attempts += 1
            if n < random_number:
                print("Too low! Try again.")
            elif n > random_number:
                print("Too high! Try again.")
            else:
                print("Congratulations, ",player_name,"! You've guessed the number ",random_number," in ",attempts," attempts.")
                break
    break

    if attempts == max_attempts:
        print("Sorry, ",player_name,", you've run out of attempts. The number was ",random_number,".")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing. Goodbye!")
            break
