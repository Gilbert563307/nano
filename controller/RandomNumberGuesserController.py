import random
from colorama import Fore
from helpers.Helpers import Helpers


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
            computer_generated_random_inter: int = random.randint(
                lowest_guessable_number, highest_guessable_number
            )
            return computer_generated_random_inter
        except Exception as e:
            print(f"An error occurred [getRandomIntBetweenTwoNumbers]: {e}")

    def informUserAboutTheRemaningChancesLeftToGuessNumber(
        selfm, number_of_times_user_can_guess: int, times_to_guess: int
    ) -> None:
        try:
            times_to_guess_calculated = number_of_times_user_can_guess - times_to_guess
            print(
                f"Je hebt nog {times_to_guess_calculated} {'pogingen' if times_to_guess_calculated > 1 else 'poging'}."
            )

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

    def run(self):
        try:
            # rand om getaal.
            # Laat de computer een random integer bepalen. (check)
            # Bepaal hoe vaak de gebruiker mag raden en hoe hoog het getal maximaal mag zijn. (check)
            # Gebruik een for-loop om de gebruiker een x-aantal keer te laten raden.(check)
            # Communiceer aan de gebruiker hoe vaak de gebruiker mag raden en of het getal al wel of niet geraden is.(check)

            lowest_guessable_number: int = 0
            highest_guessable_number: int = 15

            self.printIntroMessageToUser(
                lowest_guessable_number, highest_guessable_number
            )
            computer_generated_random_inter: int = self.getRandomIntBetweenTwoNumbers(
                lowest_guessable_number, highest_guessable_number
            )

            # times user can guess
            number_of_times_user_can_guess: int = 5
            print(f"Je krijgt 5 pogingen \n")

            # set variable to track is user has guessed the number correct, this is added for message tracking
            has_user_won_game: bool = False

            for times_to_guess in range(number_of_times_user_can_guess):

                # tell user how many guesses he still has left
                self.informUserAboutTheRemaningChancesLeftToGuessNumber(
                    number_of_times_user_can_guess, times_to_guess
                )

                guessed_number: int = self._getHelpersService().askUserForNumber()

                has_user_guessed_correct: bool = self.checkGuessedNumber(
                    guessed_number, computer_generated_random_inter
                )

                # check if user has guessed the number correct
                if has_user_guessed_correct:
                    # set the tracking state to true
                    has_user_won_game = True
                    print(Fore.GREEN + "Je heb het getaal correct geraden!!!! ")

                    # end foor loop then if user has guessed the number
                    break
                elif has_user_guessed_correct == False:
                    message: str = (
                        "Je heb het getal niet goed geraden probeer het nog een keer.\n"
                    )
                    self._getHelpersService().printColouredMessage(message, Fore.YELLOW)

            # if the user has not guessed the number correct
            if has_user_won_game == False:
                print("\n")
                self._getHelpersService().printColouredMessage(
                    "Je heb het nummer niet geraden.", color=Fore.RED
                )

            # closing meessage
            print("Het spel sluit zich nu af.\n")
            # Print NANOXL games options
            self._getHelpersService().printGameOptionsToUser(header=True)
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [RandomNumberGuesserController-run]: {e}")
