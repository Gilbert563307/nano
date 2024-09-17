from colorama import Fore, Style
import os
from datetime import date
from config import config
from art import tprint


class Helpers:

    def __init__(self) -> None:
        pass

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

    def printGameOptionsToUser(self, header: bool = False):
        if header:
            tprint("Nano App Store")
            print(
                Fore.GREEN
                + "Hier kan je een keuze maken voor welke type game je wilt spelen.\n"
            )
            self.resetTerminalColour()
        messages: list = [
            f"Kies ({config.GUESS_THE_NUMBER_REQUEST}) voor raad het getal?",
            f"Kies ({config.DIARY_REQUEST}) voor je persoonlijke dagboek",
            f"Kies ({config.HANG_MAN_REQUEST}) voor Galgje",
            f"Kies ({config.GUI_REQUEST}) voor de GUI",
            f"Kies ({config.GUESS_THE_NUMBER_BY_COMPUTER_REQUEST}) voor raad het getal, die door de computer wordt gespeeld.",
            f"Kies ({config.CLOSE_REQUEST}) om het nano appstore af te sluiten\n",
        ]

        for message in messages:
            print(message)

    def checkIfUserInputIsAValidInt(self, user_input: str) -> bool:
        # only checks if  input is not empty
        if user_input == "":
            return False

        # only checks if its a integer
        if user_input.isnumeric() == False:
            return False

        return True

    def resetTerminalColour(self) -> None:
        print(Style.RESET_ALL)

    def printColouredMessage(self, message, color) -> None:
        print(color + message)
        self.resetTerminalColour()

    def getCurrentWorkingDirFolderPath(self) -> str:
        try:
            cur_path: str = os.getcwd()
            return cur_path
        except Exception as e:
            # Handles the exception
            print(f"An error [getCurrentWorkingDirFolderPath]: {e}")
