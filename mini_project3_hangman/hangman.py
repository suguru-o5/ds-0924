import random
import constants as cnst


def main():
    print("Welcome to Hangman!")
    print("")

    game_level = determine_game_level()
    print(f"Let's start {cnst.level_to_display_name[game_level]}!")
    print("")

    # Prepare some requirements to process
    answer = prepare_answer(game_level)
    incorrect_guesses_remaining = prepare_incorrect_guesses_remaining()
    processing_letter_list = prepare_processing_letter_list(answer)
    usedletter_to_index_list = prepare_usedletter_to_index_list(answer)
    guessed_letter_list = []

    while True:
        # Game over logic
        if incorrect_guesses_remaining == 0:
            print(f"Game over! The word was: '{answer}'")
            break
        # Game clear logic
        if not any(usedletter_to_index_list):
            print(f"Congratulations! You guessed the word: '{answer}'")
            break

        # Print current word
        print("Current word: ", end="")
        print(" ".join(processing_letter_list))

        # Print guessed letters
        print("Guessed letters: ", end="")
        print(", ".join(guessed_letter_list))

        # Print incorrect guess remaining
        print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")

        input_letter = validated_input_letter(guessed_letter_list)
        guessed_letter_list.append(input_letter)

        if usedletter_to_index_list.get(input_letter) is None:
            print(f"Sorry, '{input_letter}' is not in the word.")
            print("")
            incorrect_guesses_remaining -= 1
        else:
            print(f"Good job! '{input_letter}' is in the word.")
            print("")

            # Replace the hidden letter(s) in the processing letter list
            # with the guessed letter
            for to_be_replaced_index in usedletter_to_index_list[input_letter]:
                processing_letter_list[to_be_replaced_index] = input_letter
            # Delete the key and value which is completed to replace
            del usedletter_to_index_list[input_letter]


def determine_game_level():
    while True:
        print("Select the game level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        input_game_level = input("Input the level by number: ")

        if not input_game_level in cnst.level_to_word_list.keys():
            print("Please input 1, 2, or 3")
            print("")
            continue
        else:
            return input_game_level


def prepare_answer(game_level: str):
    word_list = cnst.level_to_word_list[game_level]
    return random.choice(word_list)


def prepare_incorrect_guesses_remaining():
    # Traditionally, 8 is common because a hangman can be drawn with eight parts.
    return 8


def prepare_processing_letter_list(answer: str):
    return ["_"] * len(answer)


def prepare_usedletter_to_index_list(answer: str):
    # Key:letters used in the answer, Value:a list of the indexes
    usedletter_to_index_list: dict = {}

    for i in range(len(answer)):
        # Add a key with an empty list when the key doesn't exist in the dict.
        if not answer[i] in usedletter_to_index_list.keys():
            usedletter_to_index_list[answer[i]] = []
        usedletter_to_index_list[answer[i]].append(i)

    return usedletter_to_index_list


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
