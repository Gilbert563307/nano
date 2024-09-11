from helpers.Helpers import Helpers
from model.HangManModel import HangManModel
from config import config
import re

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

    def printHangManGameOptions(self) -> None:
        try:
            # print user options to screen
            print("Kies (1) om Galgje te spelen met makkelijke woorden.")
            print("Kies (2) om Galgje te spelen met gemiddelde woorden.")
            print("Kies (3) om Galgje te spelen met moeilijke woorden.")
            print("Kies (4) om Galgje te spelen met moeilijke woorden.\n")
        except Exception as e:
            print(f"An error occurred [printHangManGameOptions]: {e}")

    def run(self) -> None:
        try:
            self.printHangManGameOptions()
            showing_options_to_user: bool = True

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
            word_to_guess: str = random.choice(words).lower()

            # Set user tries
            TRIES_UNTIL_GAME_STOPS: int = 7

            # vertel gebruiker hoeveel pogingen die heeft
            self._getHelpersService().printColouredMessage(
                f"Je heb nog {TRIES_UNTIL_GAME_STOPS} pogingen.",
                Fore.LIGHTGREEN_EX,
            )

            # TODO remove after testing Print health bar, word, ascii hangman,
            print("Word:", word_to_guess, "\n")

            # print game status]
            self.printBeginingGameStats(word_to_guess, TRIES_UNTIL_GAME_STOPS)

            # create orrect_guessed_chars list
            correct_guessed_chars = []

            # game logic here
            for x in range(0, TRIES_UNTIL_GAME_STOPS):
                # get letter from user
                character: str = self.askUserForLetter()

                # if the chacter is the word and the character is not already gussed by the user
                if (
                    character in word_to_guess
                    and character not in correct_guessed_chars
                ):
                    # get correct gussed characters
                    self.getCorrectGuessedCharacters(
                        character, word_to_guess, correct_guessed_chars
                    )

                    # get game stats
                stats: dict = self.getGameStats(
                    word_to_guess, character, correct_guessed_chars
                )
                self._getHelpersService().printColouredMessage(
                    stats["message"], Fore.BLUE
                )

                # check if the the player has already gussed the word
                player_has_won_game: bool = self.checkIfPlayerHasWonGame(
                    stats["word"], word_to_guess
                )

                if player_has_won_game:
                    message: str = "Je heb gewonnen"
                    self._getHelpersService().printColouredMessage(message, Fore.GREEN)
                    # end game loop
                    TRIES_UNTIL_GAME_STOPS = 0
                    self.printHangManGameOptions()
                    return

                # if charactet is not in word
                if character not in word_to_guess:
                    # TODO finish game logic if user hasnt gotten the word right
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
                user_input: str = input("Vul hier een karakter in:")

                # if user option is blank
                if user_input == "":
                    self._getHelpersService().printColouredMessage(
                        "Je naam mag niet leeg zijn\n", Fore.RED
                    )

                # if user character lenght is over 1
                if len(user_input) > 1:
                    self._getHelpersService().printColouredMessage(
                        "Je mag slechts één karakter per keer invoeren.", Fore.RED
                    )

                if len(user_input) == 1:
                    return user_input.lower()

        except Exception as e:
            print(f"An error occurred [askUserForLetter]: {e}")

    def getAlfabetToDisplay(self) -> str:
        try:
            # create a list of the alphabet in uppercase
            alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        except Exception as e:
            print(f"An error occurred [getAlfabetToDisplay]: {e}")

    def getCorrectGuessedCharacters(
        self, character: str, word_to_guess: str, correct_guessed_chars: list[str]
    ) -> list[str]:
        try:

            # check if the occurence of the string is more than onece
            string_occurence_in_word_to_guess: int = word_to_guess.count(character)

            # if the user input character is more than once in the word to guess
            if string_occurence_in_word_to_guess > 1:
                for occurence in range(0, string_occurence_in_word_to_guess):
                    # append that character multiple times
                    correct_guessed_chars.append(character)
            else:
                # append only once
                correct_guessed_chars.append(character)

        except Exception as e:
            print(f"An error occurred [getCorrectGuessedCharacters]: {e}")

    def checkIfPlayerHasWonGame(
        self, guessed_word: list[str], word_to_guess: str
    ) -> bool:
        try:
            # check if that word matches the word to guess
            if guessed_word == word_to_guess:
                return True

            # else return false
            return False

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

    def getWordPositions(self, word_to_guess: str) -> list[dict]:
        try:
            dict_data: list[dict] = []

            pos = -1
            for char in word_to_guess:
                pos += 1
                data = {"pos": pos, "char": char}
                dict_data.append(data)

            return dict_data
        except Exception as e:
            print(f"An error occurred [getWordPositions]: {e}")

    def getGameStats(
        self, word_to_guess: str, user_inputted_character, all_ready_guessed_chars
    ) -> dict:
        try:
            # get the positions of each letter in the word to guess
            word_postions: list[dict] = self.getWordPositions(word_to_guess)

            # create the underscores to show to ther user
            keybaord_len_word: str = ""

            # set the _undercores for how many chars are in the word
            for char in word_to_guess:
                keybaord_len_word += "_"

            # create a list from the underscores, because we want to change the index/position of the underscore with the correct character
            list_keybaord_len_word = list(keybaord_len_word)

            #loop through all the dict data with the character and each position index
            for dict_data in word_postions:
                #loop through the already guessed chars
                for char in all_ready_guessed_chars:
                    #if char in already gussed char macthes
                    if char == dict_data["char"]:
                        #get the postion of that character from the dict
                        position = dict_data["pos"]
                        #replace the underscore with the positon u got from the dict with the charcter that is already gussed
                        list_keybaord_len_word[position] = f"{char}"

            # join that list together with spaces instead of underscores
            joined_list_word = " ".join(list_keybaord_len_word)

            # create message
            message: str = f"Woord: {joined_list_word} \n"

            #return dict with the word join together instead of with spaces
            return {"word": "".join(list_keybaord_len_word), "message": message}

        except Exception as e:
            print(f"An error occurred [printGameStats]: {e}")
