from colorama import Fore, Style
import os
from datetime import date


class Helpers:

    def __init__(self) -> None:
        pass
    
    def getTodaysDate() -> str:
        try:
            today = date.today()

            # get date in (ducth) day/month/year
            date_str: str = today.strftime("%d-%m-%Y")
            return date_str
        except Exception as e:
            print(f"An error occurred [getTodaysDate]: {e}")


    def printGameOptionsToUser(self, header: bool = False):
        if header:
            print(
                Fore.GREEN
                + "Hier kan je een keuze maken voor welke type game je wilt spelen.\n"
            )
            self.resetTerminalColour()
        messages: list = [
            "Kies (1) voor Raad het getal?",
            "Kies (2) voor je persoonlijke dagboek",
            "Kies (3) voor Galgje",
            "Kies (10) om het nano appstore af te sluiten\n",
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
