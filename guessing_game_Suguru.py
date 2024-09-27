import random

answer = random.randint(1, 1000)
guess_count = 0

from_number = 1
to_number = 1000

while True:
    guess_number = input(f"Enter your guess from {from_number} to {to_number}: ")
    
    # Check if the input value is a valid int.
    try:
        guess_number = int(guess_number)
    except ValueError:
        print("It's not a valid number. Please input your guess again.")
        continue
    
    # Check if the input value is out of range.
    if guess_number < from_number or to_number < guess_number:
        print("Out of range. Please input your guess again.")
        continue
    
    guess_count += 1
    
    if answer == guess_number:
        print(f"You got it! The hidden number is {answer}.")
        print(f"It took you took {guess_count} guess(es).")
        break
    else:
        print(f"Wrong! Guess count: {guess_count}.")
        
        # Update the range.
        if answer < guess_number:
            to_number = guess_number
        elif guess_number < answer:
            from_number = guess_number 
