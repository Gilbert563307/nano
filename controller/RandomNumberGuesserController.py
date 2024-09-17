import random
from colorama import Fore
from helpers.Helpers import Helpers
import time


class RandomNumberGuesserController:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def printIntroMessageToUser(
        self, lowest_guessable_number: int, highest_guessable_number: int
    ) -> None:
        try:
            print(
                f"Raad het getaal tussen de {lowest_guessable_number} en {highest_guessable_number} \n"
            )
        except Exception as e:
            print(f"An error occurred [printIntroMessageToUser]: {e}")

    def getRandomIntBetweenTwoNumbers(
        self, lowest_guessable_number: int, highest_guessable_number: int
    ) -> None:
        try:
            random_number: int = random.randint(
                lowest_guessable_number, highest_guessable_number
            )
            return random_number
        except Exception as e:
            print(f"An error occurred [getRandomIntBetweenTwoNumbers]: {e}")

    def informUserAboutTheRemaningChancesLeftToGuessNumber(
        self, number_of_times_user_can_guess: int, times_to_guess: int
    ) -> None:
        try:
            times_to_guess_calculated = number_of_times_user_can_guess - times_to_guess
            tries: str = "pogingen"

            if times_to_guess_calculated == 1:
                tries: str = "poging"

            message: str = f"Je heb nog {times_to_guess_calculated} {tries} \n"

            self._getHelpersService().printColouredMessage(message, Fore.BLUE)

        except Exception as e:
            print(
                f"An error occurred [informUserAboutTheRemaningChancesLeftToGuessNumber]: {e}"
            )

    def checkGuessedNumber(self, user_input: str, number_to_guess: int) -> bool:
        try:
            # check if input is een number
            if user_input == number_to_guess:
                return True
            return False
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [checkGuessedNumber]: {e}")

    def printHintsToUser(
        self, guessed_number: int, random_generated_number: int
    ) -> None:
        try:
            if guessed_number > random_generated_number:
                message: str = "[Hint] Het getal is lager."
            else:
                message: str = "[Hint] Het getal is hoger"
            self._getHelpersService().printColouredMessage(message, Fore.YELLOW)
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [checkGuessedNumber]: {e}")

    def runGameByComputerBot(self):
        try:
            LOWEST_GUESSABLE_NUMBER: int = 0
            HIGHEST_GUESSABLE_NUMBER: int = 20

            correct_number_to_guess: int = self.getRandomIntBetweenTwoNumbers(
                LOWEST_GUESSABLE_NUMBER, HIGHEST_GUESSABLE_NUMBER
            )

            # times bot can guess
            number_of_times_bot_can_guess: int = 8

            # game logic
            results: dict = self.handleBotGameLogic(
                number_of_times_bot_can_guess,
                correct_number_to_guess,
                LOWEST_GUESSABLE_NUMBER,
                HIGHEST_GUESSABLE_NUMBER,
            )

            if results["won"]:
                self._getHelpersService().printColouredMessage(
                    results["message"], Fore.GREEN
                )
            else:
                self._getHelpersService().printColouredMessage(
                    results["message"], Fore.RED
                )

            self.printClosingMessageWithOptions()
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [runGameByComputerBot]: {e}")

    def run(self):
        try:
            LOWEST_GUESSABLE_NUMBER: int = 0
            HIGHEST_GUESSABLE_NUMBER: int = 15

            self.printIntroMessageToUser(
                LOWEST_GUESSABLE_NUMBER, HIGHEST_GUESSABLE_NUMBER
            )

            correct_number_to_guess: int = self.getRandomIntBetweenTwoNumbers(
                LOWEST_GUESSABLE_NUMBER, HIGHEST_GUESSABLE_NUMBER
            )

            number_of_times_user_can_guess: int = 5

            # game logic
            results: dict = self.handleGameLogic(
                number_of_times_user_can_guess, correct_number_to_guess
            )

            if results["won"]:
                self._getHelpersService().printColouredMessage(
                    results["message"], Fore.GREEN
                )
            else:
                self._getHelpersService().printColouredMessage(
                    results["message"], Fore.RED
                )

            self.printClosingMessageWithOptions()
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [RandomNumberGuesserController-run]: {e}")

    def printClosingMessageWithOptions(self) -> None:
        try:
            # closing meessage
            print()
            self._getHelpersService().printColouredMessage(
                "Het spel sluit zich nu af.\n", Fore.MAGENTA
            )

            # Print NANOXL games options
            self._getHelpersService().printGameOptionsToUser(header=True)
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [printClosingMessageWithOptions]: {e}")

    def handleBotGameLogic(
        self,
        number_of_times_bot_can_guess: int,
        correct_number_to_guess: int,
        lowest_guessable_number: int,
        highest_guessable_number: int,
    ) -> dict[str:str, str:bool]:
        try:
            for times_to_guess in range(number_of_times_bot_can_guess):
                # make loop go slower by 2 seconds
                time.sleep(2)

                # tell bot how many guesses it has
                self.informUserAboutTheRemaningChancesLeftToGuessNumber(
                    number_of_times_bot_can_guess, times_to_guess
                )

                # make computer guess random numbber
                computer_guessed_number: int = self.getRandomIntBetweenTwoNumbers(
                    lowest_guessable_number, highest_guessable_number
                )

                has_bot_guessed_correct: bool = self.checkGuessedNumber(
                    computer_guessed_number, correct_number_to_guess
                )

                # check if bot has gussed nunber correct
                if has_bot_guessed_correct:
                    message: str = "De bot heeft het getal goed geraden.\n"
                    return {"message": message, "won": True}
                else:
                    message: str = (
                        "De bot heeft het getal niet goed geraden en probeert het nu opnieuw.\n"
                    )
                    self._getHelpersService().printColouredMessage(message, Fore.YELLOW)

            return {"message": "De bot heeft het nummer niet geraden.", "won": False}
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [handleBotGameLogic]: {e}")

    def handleGameLogic(
        self,
        number_of_times_user_can_guess: int,
        correct_number_to_guess: int,
    ) -> dict:
        try:
            for times_to_guess in range(number_of_times_user_can_guess):

                self.informUserAboutTheRemaningChancesLeftToGuessNumber(
                    number_of_times_user_can_guess, times_to_guess
                )

                guessed_number: int = self._getHelpersService().askUserForNumber()

                has_user_guessed_correct: bool = self.checkGuessedNumber(
                    guessed_number, correct_number_to_guess
                )

                self.printHintsToUser(guessed_number, correct_number_to_guess)

                # check if user has guessed the number correct
                if has_user_guessed_correct:

                    # end foor loop then if user has guessed the number
                    return {
                        "message": "Je heb het getaal correct geraden!!!! ",
                        "won": True,
                    }
                else:
                    message: str = (
                        "Je heb het getal niet goed geraden probeer het nog een keer.\n"
                    )
                    self._getHelpersService().printColouredMessage(message, Fore.YELLOW)

            return {"message": "Je heb het nummer niet geraden.", "won": False}
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [handleGameLogic]: {e}")
