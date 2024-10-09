from colorama import Fore, Style
import os
import platform
from datetime import date
from config import config
from art import tprint
from pathlib import Path


class Helpers:

    def __init__(self) -> None:
        pass

    def getEnvVar(self, var: str) -> str | int | float:
        try:
            return os.getenv(var)
        except Exception as e:
            print(f"An error occurred [getEnvVar]: {e}")

    def askUserForNumber(self) -> int:
        try:
            while True:
                # get user input
                option: str = input("Vul hier het getal in: \n")

                # if user option is blank
                if option.strip() == "":
                    message = "Je keuze mag niet leeg zijn.\n"
                    self.printColouredMessage(message, Fore.RED)
                    continue

                # Check if the input is numeric
                if option.strip().isnumeric():
                    return int(option)
                else:
                    message: str = "Voer een geldig getal in.\n"
                    self.printColouredMessage(message, Fore.RED)

        except Exception as e:
            print(f"An error occurred [askUserForNumber]: {e}")

    def getTodaysDate(self) -> str:
        try:
            today = date.today()

            # get date in (ducth) day/month/year
            date_str: str = today.strftime("%d/%m/%Y")
            return date_str
        except Exception as e:
            print(f"An error occurred [getTodaysDate]: {e}")

    def printGameOptionsToUser(self, header: bool = False, clear_console: bool = False):
        try:
            if clear_console:
                self.clearConsole()

            if header:
                tprint(f"{config.APP_NAME}")
                print(
                    Fore.GREEN
                    + "Hier kan je een keuze maken voor welke type game je wilt spelen.\n"
                )
                self.resetTerminalColour()
            messages: list = [
                f"Kies ({config.GUESS_THE_NUMBER_REQUEST}) voor raad het getal?",
                f"Kies ({config.DIARY_REQUEST}) voor je persoonlijke dagboek",
                f"Kies ({config.HANG_MAN_REQUEST}) voor galgje",
                f"Kies ({config.GUI_REQUEST}) voor de GUI",
                f"Kies ({config.GUESS_THE_NUMBER_BY_COMPUTER_REQUEST}) voor raad het getal, die door de computer wordt gespeeld.",
                f"Kies ({config.HANG_MAN_BY_COMPUTER_REQUEST}) voor galgje, die door de computer wordt gespeeld.",
                f"Kies ({config.SUDOKU_REQUEST}) voor sudoku.",
                f"Kies ({config.CLOSE_REQUEST}) om de nano appstore af te sluiten. \n",
            ]

            for message in messages:
                print(message)

        except Exception as e:
            print(f"An error occurred [printGameOptionsToUser]: {e}")

    def checkIfUserInputIsAValidInt(self, user_input: str) -> bool:
        try:
            # only checks if  input is not empty
            if user_input == "":
                return False

            # only checks if its a integer
            if user_input.isnumeric() == False:
                return False

            return True
        except Exception as e:
            # Handles the exception
            print(f"An error [checkIfUserInputIsAValidInt]: {e}")

    def resetTerminalColour(self) -> None:
        print(Style.RESET_ALL)

    def printColouredMessage(self, message, color) -> None:
        print(color + message)
        self.resetTerminalColour()

    def getCurrentWorkingDirFolderPath(self) -> str:
        try:
            # Get the directory where the script is located this: returns the model folder
            script_path = os.path.dirname(os.path.abspath(__file__))
            # remove the model name from tha pag
            current_dir_path = script_path[: len(script_path) - 7]
            return current_dir_path
        except Exception as e:
            # Handles the exception
            print(f"An error [getCurrentWorkingDirFolderPath]: {e}")

    def clearConsole(self):
        try:
            # Detect the current OS
            current_os = platform.system()

            # Run the appropriate command
            if current_os == "Windows":
                os.system("cls")
            else:
                os.system("clear")
        except Exception as e:
            # Handles the exception
            print(f"An error [clearConsole]: {e}")
