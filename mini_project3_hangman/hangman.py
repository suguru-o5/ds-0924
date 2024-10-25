import random


def main():
    answer = prepare_answer()
    incorrect_guesses_remaining = prepare_incorrect_guesses_remaining(answer)

    print("Welcome to Hangman!")

    status_dict = prepare_status_dict(answer)

    guessed_letter_list = []

    while True:
        # Game over logic
        if incorrect_guesses_remaining == 0:
            print(f"Game over! The word was: {answer}")
            break
        # Game clear logic
        if not False in status_dict.values():
            print(f"Congratulations! You guessed the word: {answer}")
            break

        # Print current word
        print("Current word: ", end="")
        for letter in list(answer):
            print_letter = letter if status_dict.get(letter) else "_"
            print(print_letter, end="")
            print(" ", end="")
        print("")

        # Print guessed letters
        print("Guessed letters: ", end="")
        for letter in guessed_letter_list:
            print(letter, end="")
            print(", ", end="")
        print("")

        print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")

        input_letter = validated_input_letter(guessed_letter_list)
        guessed_letter_list.append(input_letter)

        if status_dict.get(input_letter) is None:
            print(f"Sorry, {input_letter} is not in the word.")
            print("")
            incorrect_guesses_remaining -= 1
        else:
            print(f"Good job! {input_letter} is in the word.")
            print("")
            status_dict[input_letter] = True


def prepare_answer():
    words = ["python", "java", "go", "typescript", "php", "javascript"]

    random_int = random.randrange(0, len(words) - 1)
    return words[random_int]


def prepare_incorrect_guesses_remaining(answer: str):
    return len(answer)


def prepare_status_dict(answer: str):
    letter_list = list(answer)
    status_dict = {}

    for char in letter_list:
        status_dict[char] = False

    return status_dict


def validated_input_letter(guessed_letter_list: list):
    import re

    r = re.compile("^[a-zA-Z]*$")

    while True:
        user_input = input("Guess a letter: ")

        # Empty check
        if len(user_input) == 0:
            print("Empty value is not acceptable. Please try again.")
            continue

        # Length check
        if 1 < len(user_input):
            print("Only one alphabet is acceptable. Please try again.")
            continue

        # Pattern matching
        if not r.match(user_input):
            print("Only alphabet is acceptable. Please try again.")
            continue

        lower_letter = user_input.lower()

        # Duplicate check
        if lower_letter in guessed_letter_list:
            print("You have already guessed that letter. Please try another letter.")
            continue

        return lower_letter


if __name__ == "__main__":
    main()
