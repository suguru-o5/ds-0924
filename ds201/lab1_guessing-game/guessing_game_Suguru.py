import random

answer = random.randint(1, 1000)
guess_count = 0
lower_limit = 1
upper_limit = 1000

while True:
    guess_number = input(f"Enter your guess from {lower_limit} to {upper_limit}: ")

    # Check if the input value is a valid int.
    try:
        guess_number = int(guess_number)
    except ValueError:
        print("It's not a valid number. Please input your guess again.")
        continue

    # Check if the input value is out of range.
    if not lower_limit <= guess_number <= upper_limit:
        print("Out of range. Please input your guess again.")
        continue

    guess_count += 1

    if answer == guess_number:
        print(f"You got it! The hidden number is {answer}.")
        print(f"It took you {guess_count} guess(es).")
        break
    else:
        print(f"Wrong! Guess count: {guess_count}.")

        # Update the range.
        if answer < guess_number:
            upper_limit = guess_number - 1
        elif guess_number < answer:
            lower_limit = guess_number + 1
