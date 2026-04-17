import random

# Message Information

def main():
    target = random.randint(1, 100)
    attempt_count = 0

    print("Welcome to Guess The Number")
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempt_count += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempt_count} attempts.")
            break



if __name__ == "__main__":
    main()