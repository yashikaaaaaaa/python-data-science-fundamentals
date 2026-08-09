import random

secret = random.randint(1, 20)

attempts = 5

while attempts > 0:

    guess = int(input("Guess the Number (1-20): "))

    if guess == secret:
        print("🎉 Congratulations! You guessed correctly.")
        break

    elif guess > secret:
        print("Too High!")

    else:
        print("Too Low!")

    attempts -= 1
    print(f"Attempts Left : {attempts}")

if attempts == 0:
    print(f"\nGame Over! The number was {secret}.")