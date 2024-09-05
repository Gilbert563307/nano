import random

# import sys
from colorama import Fore, Style

from helpers.Helpers import Helpers


class RandomNumberGuesserController:
    # initilianze
    def __init__(self):
        self.helper = None
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def run(self):
        try:
            # rand om getaal.
            # Laat de computer een random integer bepalen. (check)
            # Bepaal hoe vaak de gebruiker mag raden en hoe hoog het getal maximaal mag zijn. (check)
            # Gebruik een for-loop om de gebruiker een x-aantal keer te laten raden.(check)
            # Communiceer aan de gebruiker hoe vaak de gebruiker mag raden en of het getal al wel of niet geraden is.(check)

            lowest_guessable_number: int = 0
            highest_guessable_number: int = 15

            # random number between 0,15 both included
            print(
                f"Raad het getaal tussen de {lowest_guessable_number} en {highest_guessable_number} \n"
            )

            computer_generated_random_inter: int = random.randint(
                lowest_guessable_number, highest_guessable_number
            )

            # times user can guess
            number_of_times_user_can_guess: int = 5
            print(f"Je krijgt 5 pogingen \n")

            # set variable to track is user has guessed the number correct, this is added for message tracking
            has_user_guessed_the_number: bool = False
            for times_to_guess in range(number_of_times_user_can_guess):

                # tell user how many guesses he still has left
                times_to_guess_calculated = (
                    number_of_times_user_can_guess - times_to_guess
                )
                print(
                    f"Je hebt nog {times_to_guess_calculated} {'pogingen' if times_to_guess_calculated > 1 else 'poging'}."
                )

                guessed_number: int = input("Vul hier het getal in: \n")
                results = self._getHelpersService().checkGuessedNumber(
                    guessed_number, computer_generated_random_inter
                )

                # check if user has guessed the number correct
                if results == True:
                    # set the tracking state to true
                    has_user_guessed_the_number = True
                    print(Fore.GREEN + "Je heb het getaal correct geraden!!!! ")

                    # end foor loop then if user has guessed the number
                    break

            # if the user has not guessed the number correct
            if has_user_guessed_the_number == False:
                print("\n")
                self._getHelpersService().printColouredMessage("Je heb het nummer niet geraden.", color=Fore.RED)

            # closing meessage
            print("Het spel sluit zich nu af.\n")
            # TODO ASK IF NEEDED TO END GAME, because main gameloop is still running in NanoXLController IN LES
            self._getHelpersService().printGameOptionsToUser(header=True)
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [RandomNumberGuesserController-run]: {e}")
