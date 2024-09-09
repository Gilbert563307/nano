from helpers.Helpers import Helpers
from model.HangManModel import HangManModel
from config import config

from colorama import Fore
import random


class HangManController:

    def __init__(self) -> None:
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def _getHangManModel(self) -> HangManModel:
        return HangManModel()

    def getEasyHangManWords(self) -> list[str]:
        try:
            makkelijke_woorden_key: int = config.EASY_WORDS_OPTION
            response: dict = self._getHangManModel().getHangManWords(
                makkelijke_woorden_key
            )

            # check for errors
            if response["error"]:
                self._getHelpersService().printColouredMessage(
                    response["message"], Fore.RED
                )
                return []

            return response["words"]
        except Exception as e:
            print(f"An error occurred [getEasyHangManWord]: {e}")

    def getHangManAscii(self):
        try:
            HANGMANPICS = [
                """
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                /|   |
                    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                /|\  |
                    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                /|\  |
                /    |
                    |
                =========""",
                """
                +---+
                |   |
                O   |
                /|\  |
                / \  |
                    |
                =========""",
            ]
            return HANGMANPICS
        except Exception as e:
            print(f"An error occurred [getHangManAscii]: {e}")

    def getAverageHangManWords(self) -> list[str]:
        try:
            gemiddelde_woorden_key: int = config.AVERAGE_WORDS_OPTION
            response: dict = self._getHangManModel().getHangManWords(
                gemiddelde_woorden_key
            )

            # check for errors
            if response["error"]:
                self._getHelpersService().printColouredMessage(
                    response["message"], Fore.RED
                )
                return []

            return response["words"]

        except Exception as e:
            print(f"An error occurred [getAverageHangManWords]: {e}")

    def getHardHangManWords(self) -> list[str]:
        try:
            moeilijke_woorden_key: int = config.HARD_WORDS_OPTION
            response: dict = self._getHangManModel().getHangManWords(
                moeilijke_woorden_key
            )

            # check for errors
            if response["error"]:
                self._getHelpersService().printColouredMessage(
                    response["message"], Fore.RED
                )
                return []

            return response["words"]
        except Exception as e:
            print(f"An error occurred [getHardHangManWords]: {e}")

    def getHangManOptions(self) -> list[str]:
        try:
            END_GAME_OPTION: str = 4
            available_options: list[int] = config.HANG_MAN_WORD_DIFFICULTY_OPTIONS

            # add the end game option to the list
            return available_options + [4]
        except Exception as e:
            print(f"An error occurred [getHangManOptions]: {e}")

    def run(self) -> None:
        try:
            showing_options_to_user: bool = True
            # print user options to screen
            print("Kies (1) om Galgje te spelen met makkelijke woorden.")
            print("Kies (2) om Galgje te spelen met gemiddelde woorden.")
            print("Kies (3) om Galgje te spelen met moeilijke woorden.")
            print("Kies (4) om Galgje te spelen met moeilijke woorden.\n")

            while showing_options_to_user:
                chosen_option: int = self.askUserForChosenHangmanOption()

                if (
                    chosen_option == 4
                ):  # reffers to END_GAME_OPTION should actually be in a config folder but no
                    message: str = "Het spel wordt nu afgelosten \n"
                    self._getHelpersService().printColouredMessage(message, Fore.RED)
                    self._getHelpersService().printGameOptionsToUser()
                    break

                # ask for user name, this code will run until user fills a name in
                user_name = self.askUserForHisName()

                if user_name:
                    # chosen with easy words
                    if chosen_option == 1:
                        self.continueHangManWithEasyOptionsGameMode()
                        break

                pass
        except Exception as e:
            print(f"An error occurred [run][HangManController]: {e}")

    def getHangManHealthBar(self, number_of_tries: int) -> str:
        try:
            # heart game user
            heart_emoji: str = "❤️"

            # broken heart:
            broken_heart: str = "💔"
            health_bar: str = ""
            for number in range(0, number_of_tries):
                health_bar += f"{heart_emoji} "
            return health_bar
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManHealthBar]: {e}")

    def continueHangManWithEasyOptionsGameMode(self) -> None:
        try:
            # Fetch the words
            words: list[str] = self.getEasyHangManWords()

            # if words array is empty end game
            if len(words) == 0:
                return

            # Random word
            word: str = random.choice(words).lower()

            # Set user tries
            tries_until_game_stops = len(word)

            # vertel gebruiker hoeveel pogingen die heeft
            self._getHelpersService().printColouredMessage(
                f"Je heb nog {tries_until_game_stops} pogingen. \n",
                Fore.LIGHTGREEN_EX,
            )

            # TODO remove after testing Print health bar, word, ascii hangman,
            print("Word:", word, "\n")

            # print game status]
            self.printBeginingGameStats(word, tries_until_game_stops)

            # create orrect_guessed_chars list
            correct_guessed_chars = []

            # game logic here
            for x in range(0, tries_until_game_stops):
                # get letter from user
                character: str = self.askUserForLetter()

                if character in word:
                    # save the correct guessed char into an array
                    correct_guessed_chars.append(character)

                    # print game stats
                    self.printGameStats(word, character, correct_guessed_chars)
                else:
                    #TODO finish game logic if user hasnt gotten the word right
                    print("no char in word")

        except Exception as e:
            print(f"An error occurred [continueHangManWithEasyOptionsGameMode]: {e}")

    def askUserForChosenHangmanOption(self) -> str:
        try:
            available_options: list[str] = self.getHangManOptions()

            while True:
                # get user input
                option: str = int(input(""))

                # if user option is blank
                if option == "":
                    print("Maak een keuze:\n")

                # check
                if option not in available_options:
                    print("Maak een keuze tussen 1/4")

                return option

        except Exception as e:
            print(f"An error occurred [askUserForChosenHangmanOption]: {e}")

    def askUserForHisName(self) -> str:
        try:
            while True:
                # get user input
                user_input: str = input("Vul hier je naam eerst in: \n")

                # if user option is blank
                if user_input == "":
                    self._getHelpersService().printColouredMessage(
                        "Je naam mag niet leeg zijn\n", Fore.RED
                    )

                return user_input

        except Exception as e:
            print(f"An error occurred [askUserForHisName]: {e}")

    def askUserForLetter(self) -> str:
        try:
            while True:
                # get user input
                user_input: str = input("Vul hier een karakter in: \n")

                # if user option is blank
                if user_input == "":
                    self._getHelpersService().printColouredMessage(
                        "Je naam mag niet leeg zijn\n", Fore.RED
                    )
                
                #if user character lenght is over 1
                if len(user_input) > 1:
                    self._getHelpersService().printColouredMessage(
                        "Je mag slechts één karakter per keer invoeren.", Fore.RED
                    )

                return user_input.lower()

        except Exception as e:
            print(f"An error occurred [askUserForLetter]: {e}")

    def getAlfabetToDisplay(self) -> str:
        try:
            # create a list of the alphabet in uppercase
            alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        except Exception as e:
            print(f"An error occurred [getAlfabetToDisplay]: {e}")

    def printBeginingGameStats(self, word_to_guess, tries_until_game_stops) -> str:
        try:
            # Print the hearts that the user has
            health_bar: str = self.getHangManHealthBar(tries_until_game_stops)
            print(f"Jou levens: {health_bar}\n")

            keybaord_len_word: str = ""
            # print the _ to simulate the keyboard typed words
            for char in range(0, len(word_to_guess)):
                keybaord_len_word += "_ "

            print(f"Woord: {keybaord_len_word}")
        except Exception as e:
            print(f"An error occurred [printBeginingGameStats]: {e}")

    def printGameStats(
        self, word_to_guess: str, user_inputted_character, all_ready_guessed_chars
    ) -> str:
        try:
            # create the underscores to show to ther user
            keybaord_len_word: str = ""

            # set the _undercores for how many chars are in the word
            for char in word_to_guess:
                keybaord_len_word += "_"

            # create a list from the keybaord_len_word other wise we cant change the pos of that word
            list_keybaord_len_word = list(keybaord_len_word)

            # create a list from thr word to guess so that we can get the pos of the char
            list_word_to_guess = list(word_to_guess)

            # loop through each character of the word
            for char in word_to_guess:
                # if the typed in user character is the word
                if user_inputted_character in word_to_guess:
                    # get the position of the char in the word
                    position: int = list_word_to_guess.index(user_inputted_character)

                    # go to the list of the underscores, get the position of which underscore we want to replace
                    list_keybaord_len_word[position] = f"{user_inputted_character}"

            # loop through all the characters the user has already guessed
            for char in all_ready_guessed_chars:
                # get the pos of the char that is in the created list of thr word to guess
                position: int = list_word_to_guess.index(char)
                # replace that underscore with the character
                list_keybaord_len_word[position] = f"{char}"

            # join that list together and print thr word
            joined_list_word = " ".join(list_keybaord_len_word)

            # create message
            message: str = f"Woord: {joined_list_word} \n"
            self._getHelpersService().printColouredMessage(message, Fore.BLUE)

        except Exception as e:
            print(f"An error occurred [printGameStats]: {e}")
