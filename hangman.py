from random import choice

HANGMAN = [
    "________",
    "|       |",
    "|       O",
    "|       |",
    "|      /|\ ",
    "|       |",
    "|      / \ ",
]

WORDS = [
    "CASA",
    "CARRO",
    "MONO",
    "ESTERNOCLEIDOMASTOIDEO",
    "PYTHON",
    "DJANGO",
    "MILTON",
    "LENIS",
    "SWAPPS",
    "LOGIA",
    "UNITTESTING",
]


class Hangman:
    """
    Initialise instance and create a list from word string

    :type word: str
    :param word: The word to guess
    """

    def __init__(self, word: str) -> None:
        self.failed_attempts = 0
        self.word = word
        self.word_chars = {}
        self.chars_to_guess = list("_" * len(self.word))

    """
    Create a mapping for each letter in the word to 
    guess and it's corresponding index or indexes
    """

    def _word_char_mapping(self) -> None:
        for index, char in enumerate(self.word):
            if char in self.word_chars:
                self.word_chars[char].append(index)
            else:
                self.word_chars[char] = [index]

    """
    Validate that user input is a letter

    :type input_: str
    :param input_: letter guessed by user
    """

    def is_invalid_letter(self, input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    """
    Display the game's progress
    """

    def print_game_status(self) -> None:
        print("\n")
        print("\n".join(HANGMAN[: self.failed_attempts]))
        print("\n")
        print(" ".join(self.chars_to_guess))

    """
    Take guessed letter and update the corresponding 
    index or indexes within the word that is being guesed

    :type letter: str
    :param letter: letter guessed by user
    """

    def update_progress(self, letter) -> None:
        for index in self.word_chars.get(letter):
            self.chars_to_guess[index] = letter

    """
    Prompt user to guess letter in the word
    """

    def get_user_input(self) -> str:
        user_input = input("\nPlease type a letter: ")
        return user_input

    """
    Prompt user to guess a letter and play the
    game until the word is guessed correctly or
    there isn't remaining chances for more guesses
    """

    def play(self):
        self._word_char_mapping()
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            user_input = user_input.upper() if not user_input.isupper() else user_input

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print("¡The input is not a letter!")
                continue
            # Check if the letter is not already guessed
            if user_input in self.chars_to_guess:
                print("You already have guessed that letter")
                continue

            if user_input in self.word:
                self.update_progress(user_input)
                # If there is no letter to find in the word
                if self.chars_to_guess.count("_") == 0:
                    print("\n¡Yay! You win!")
                    print("The word is: {0}".format(self.word))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")


if __name__ == "__main__":
    word_to_guess = choice(WORDS)
    print(word_to_guess)
    hangman = Hangman(word_to_guess)
    hangman.play()
