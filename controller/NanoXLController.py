from controller.RandomNumberGuesserController import RandomNumberGuesserController
from controller.DiaryController import DiaryController
from controller.HangManController import HangManController
from helpers.Helpers import Helpers
from colorama import Fore
from config import config


class NanoXLController:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def printWelcomeMessage(self):
        print(Fore.RED + "Welkom bij  App Store op nano \n")
        print(
            Fore.GREEN
            + "Hier kan je een keuze maken voor welke type game je wilt spelen."
        )
        self._getHelpersService().resetTerminalColour()
        self._getHelpersService().printGameOptionsToUser()

    def handleRequest(self, request: int):
        try:

            # create array of allowed gamemodes
            allowed_requests = [
                config.GUESS_THE_NUMBER_REQUEST,
                config.DIARY_REQUEST,
                config.HANG_REQUEST,
                config.GUI_REQUEST,
            ]

            # check if user has not made right option between in allowed_requests
            if request not in allowed_requests:
                print("Onjuiste game keuze probeer het nogmaals\n")

            # if user has made the right option
            if request in allowed_requests:

                # check of de gebruiker de game mode heeft geozen voor raad het getaal
                if request == config.GUESS_THE_NUMBER_REQUEST:
                    controller = RandomNumberGuesserController()
                    controller.run()

                # check of de gebruiker de game mode heeft gekozen voor het dagboek
                if request == config.DIARY_REQUEST:
                    controller = DiaryController()
                    controller.run()

                # check if de gebruiker game mode heeft gekozen voor hangman
                if request == config.HANG_REQUEST:
                    controller = HangManController()
                    controller.run()

                # check if de gebruiker game mode heeft gekozen voor GUI
                if request == config.GUI_REQUEST:
                    print("thinker'")
                    print("STILL WORKING ON THINKER'")

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [handleRequest]: {e}")

    def run(self):
        try:
            game_started: bool = True
            self.printWelcomeMessage()

            while game_started:

                mode_selected: int = self._getHelpersService().askUserForNumber()
                if mode_selected == config.CLOSE_REQUEST:
                    self._getHelpersService().printColouredMessage(
                        "Nano store afgesloten", Fore.MAGENTA
                    )
                    return

                self.handleRequest(mode_selected)
                # end while loop TODO if we want to keep the game loop running remove break

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [NanoXLController-run]: {e}")
