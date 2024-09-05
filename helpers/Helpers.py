from colorama import Fore, Style


class Helpers:

    def __init__(self) -> None:
        pass

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

    def checkGuessedNumber(self, user_input: int, number_to_guess: int) -> bool:
        # check of de optie gekozen leeg is en of het geen getal is
        if user_input.isnumeric() == False:
            print("De ingevoerde waarde moet een getaal zijn\n")

        if user_input == "":
            print("Het veld mag niet leeg zijn\n")

        if int(user_input) == number_to_guess:
            return True
        return False

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
