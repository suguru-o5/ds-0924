import random

level_to_word_list = {
    "easy": [
        "cat",
        "dog",
        "sun",
        "book",
        "fish",
        "tree",
        "chair",
        "house",
        "apple",
        "ball",
    ],
    "medium": [
        "engine",
        "window",
        "bottle",
        "garden",
        "pirate",
        "candle",
        "basket",
        "winter",
        "bridge",
        "monster",
    ],
    "hard": [
        "astronomy",
        "architecture",
        "knowledge",
        "revolution",
        "unbelievable",
        "adventure",
        "questionnaire",
        "persistence",
        "trampoline",
        "hypothesis",
    ],
}


def main():
    display_menu()

    answer = prepare_answer()
    incorrect_guesses_remaining = prepare_incorrect_guesses_remaining()
    processing_letter_list = prepare_processing_letter_list(answer)
    usedletter_to_index = prepare_usedletter_to_index(answer)
    guessed_letter_list = []

    while True:
        # Game over logic
        if incorrect_guesses_remaining == 0:
            print(f"Game over! The word was: '{answer}'")
            break
        # Game clear logic
        if not any(usedletter_to_index):
            print(f"Congratulations! You guessed the word: '{answer}'")
            break

        # Print current word
        print("Current word: ", end="")
        for letter in processing_letter_list:
            print(letter, end=" ")
        print("")

        # Print guessed letters
        print("Guessed letters: ", end="")
        for letter in guessed_letter_list:
            print(letter, end=", ")
        print("")

        # Print incorrect guess remaining
        print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")

        input_letter = validated_input_letter(guessed_letter_list)
        guessed_letter_list.append(input_letter)

        if usedletter_to_index.get(input_letter) is None:
            print(f"Sorry, '{input_letter}' is not in the word.")
            print("")
            incorrect_guesses_remaining -= 1
        else:
            print(f"Good job! '{input_letter}' is in the word.")
            print("")

            # Replace the blank letter in the processing letter list
            # with the guessed letter
            for to_be_replaced_index in usedletter_to_index[input_letter]:
                processing_letter_list[to_be_replaced_index] = input_letter
            del usedletter_to_index[input_letter]


def display_menu():
    print("Welcome to Hangman!")
    print("")


def determine_game_level():
    while True:
        print("Select the game level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        input_game_level = input("Input the level by number: ")
        level_definition = {"1": "easy", "2": "medium", "3": "hard"}

        if not level_definition.get(input_game_level):
            print("Please input 1, 2, or 3")
            print("")
            continue
        else:
            return level_definition[input_game_level]


def prepare_answer():
    game_level = determine_game_level()
    word_list = level_to_word_list[game_level]
    return random.choice(word_list)


def prepare_incorrect_guesses_remaining():
    # Traditionally, 8 is common because a hangman can be drawn with eight parts.
    return 8


def prepare_processing_letter_list(answer: str):
    return ["_"] * len(answer)


def prepare_usedletter_to_index(answer: str):
    usedletter_to_index: dict = {}
    for i in range(len(answer)):
        if usedletter_to_index.get(answer[i]):
            usedletter_to_index[answer[i]].append(i)
        else:
            usedletter_to_index[answer[i]] = [i]
    return usedletter_to_index


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
