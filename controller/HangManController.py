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
            makkelijke_woorden: list[str] = self._getHangManModel().getHangManWords(makkelijke_woorden_key)

            return makkelijke_woorden
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
            print(HANGMANPICS[0])
        except Exception as e:
            print(f"An error occurred [getHangManAscii]: {e}")

    def getAverageHangManWords(self) -> list[str]:
        try:
            gemiddelde_woorden_key: int = config.AVERAGE_WORDS_OPTION    
            gemiddelde_woorden: list[str] = self._getHangManModel().getHangManWords(gemiddelde_woorden_key)

            return gemiddelde_woorden
        except Exception as e:
            print(f"An error occurred [getAverageHangManWords]: {e}")

    def getHardHangManWords(self) -> list[str]:
        try:
            moeilijke_woorden_key: int = config.HARD_WORDS_OPTION    
            moeilijke_woorden = self._getHangManModel().getHangManWords(moeilijke_woorden_key)

            return moeilijke_woorden
        except Exception as e:
            print(f"An error occurred [getHardHangManWords]: {e}")

    def getHangManOptions(self) -> list[str]:
        try:
            END_GAME_OPTION: str = 4
            available_options: list[int] = config.HANG_MAN_WORD_DIFFICULTY_OPTIONS
            
            #add the end game option to the list
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

                # chosen with easy words
                if chosen_option == 1:
                    self.continueHangManWithEasyOptionsGameMode()
                    break

                pass
        except Exception as e:
            print(f"An error occurred [run][HangManController]: {e}")

    def continueHangManWithEasyOptionsGameMode(self) -> None:
        try:
            # Fetch the words
            easy_words: list[str] = self.getEasyHangManWords()
            print(f"easy_words {easy_words}")

            # Random word
            word: str = random.choice(easy_words)

            # Set user tries
            tries_until_game_stops = len(word)

            # heart game user
            heart_emoji: str = "❤️"

            # broken heart:
            broken_heart: str = "💔"

            # Print the hearts that the user has
            health_bar: str = ""
            for number in range(0, tries_until_game_stops):
                health_bar += f"{heart_emoji} "

            # Print health bar, word,
            print("Word:", word, "\n")
            print(f"Your lives: {health_bar}\n")

            while tries_until_game_stops > 0:
                # Your game logic here
                pass

        except Exception as e:
            print(f"An error occurred [continueHangManWithEasyOptionsGameMode]: {e}")

    def askUserForChosenHangmanOption(self) -> None:
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
