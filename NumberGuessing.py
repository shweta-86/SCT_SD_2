import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            # Prompt the user to input their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the user's guess to the generated number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
