from random import choice
from re import findall

from english_words import get_english_words_set


class Hangman:
    def __init__(self):
        self.tries: list = []
        self.tried_letter: list = []
        self.word: str = self.choose_difficulty().lower()
        self.hidden_word: list = ["_" for letter in self.word]

    def choose_difficulty(self) -> str:
        """
        Ask the player the difficulty in which they want to play then set the number of 
        tries they have and choose a word in the dictionary
        """
        dictionary: list = list(get_english_words_set(["web2"], lower=True))
        while True:
            difficulty = input(
                "\nPlease, choose a difficulty between 1(Easy), 2(Medium) and 3(Hard): "
            )
            try:
                match int(difficulty):
                    case 1:
                        print("\nYou have chosen the easy difficulty.")
                        self.tries.extend(["_" for t in range(8)])
                        return choice(
                            [
                                word
                                for word in dictionary
                                if len(word) > 5 and len(word) <= 9
                            ]
                        )
                    case 2:
                        print("\nYou have chosen the medium difficulty.")
                        self.tries.extend(["_" for t in range(5)])
                        return choice(
                            [
                                word
                                for word in dictionary
                                if len(word) > 4 and len(word) <= 6
                            ]
                        )
                    case 3:
                        print("\nYou have chosen the hard difficulty")
                        self.tries.extend(["_" for t in range(3)])
                        return choice([word for word in dictionary if len(word) == 3])
                    case _:
                        print("Please choose between 1, 2 and 3!")
            except ValueError:
                print("\nPlease choose between 1, 2 and 3!")

    def player_input(self) -> str:
        """Ask for the player input, check if the input is valid then return the string"""
        while True:
            letter = input("\nPlease choose one letter: ")
            if (
                letter in findall(r"[A-z]", letter.strip())
                and letter not in self.tried_letter
            ):
                self.tried_letter.append(letter)
                return letter.lower()
            elif not letter.isalpha():
                print("\nPlease choose a letter between A and z.")
            elif len(letter) != 1:
                print("\nPlease choose only one letter")
            elif letter in self.tried_letter:
                print("\nPlease choose a letter that haven't been chosen.")
            else:
                print("\nSorry, that wasn't a valid input.")


def main() -> None:
    hangman = Hangman()

    def restart() -> None:
        """Function to restart or to end the game"""
        while True:
            question = input("\nDo you wanna play again(Y/N)? ")
            if question.lower() == "y":
                main()
            elif question.lower() == "n":
                quit()
            else:
                print("Please, answer with Y or N.")

    while True:
        if "_" in hangman.tries and "_" in hangman.hidden_word:
            print(
                f"\nTries: {' '.join([item for item in hangman.tries])}"
                f"\nTried letters: {' '.join([letter for letter in hangman.tried_letter])}"
                f"\nWord: {' '.join(hangman.hidden_word)}"
            )
            letter = hangman.player_input()
            if letter in hangman.word:
                for item in list(enumerate(hangman.word)):
                    if item[1] == letter:
                        hangman.hidden_word[item[0]] = letter
            else:
                hangman.tries[hangman.tries.index("_")] = "X"
        elif "_" not in hangman.tries:
            print(
                f"\nYou lose! \nTries: {' '.join([item for item in hangman.tries])}"
                f"\nTried letters: {' '.join([letter for letter in hangman.tried_letter])}"
                f"\nThe word was: {hangman.word}"
            )
            restart()
        elif "_" not in hangman.hidden_word:
            print(
                f"\nYou won! \nTries: {' '.join([item for item in hangman.tries])}"
                f"\nTried letters: {' '.join([letter for letter in hangman.tried_letter])}"
                f"\nThe word was: {hangman.word}"
            )
            restart()


if __name__ == "__main__":
    main()
