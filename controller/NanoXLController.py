from controller.RandomNumberGuesserController import RandomNumberGuesserController
from controller.DiaryController import DiaryController
from controller.HangManController import HangManController
from helpers.Helpers import Helpers
from colorama import Fore, Style


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

    def handleRequest(self, request: str):
        try:
            # check if gamemode is number
            if request.isnumeric() == False:
                print("Vul een getaal in\n")

            # define game modes
            GUESS_THE_NUMBER_REQUEST:int = 1
            DIARY_REQUEST:int = 2
            HANG_REQUEST:int = 3

            # create array of allowed gamemodes
            allowed_requests = [GUESS_THE_NUMBER_REQUEST, DIARY_REQUEST, HANG_REQUEST]

            # print("getGameModeToPlay line 21")
            string_to_int_casted_request = int(request)

            # check if user has not made right option between 1,2,3
            if string_to_int_casted_request not in allowed_requests:
                print("Onjuiste game keuze probeer het nogmaals\n")

            # if user has made the right option
            if string_to_int_casted_request in allowed_requests:

                # check of de gebruiker de game mode heeft geozen voor raad het getaal
                if string_to_int_casted_request == GUESS_THE_NUMBER_REQUEST:
                    controller = RandomNumberGuesserController()
                    controller.run()

                # check of de gebruiker de game mode heeft gekozen voor het dagboek
                if string_to_int_casted_request == DIARY_REQUEST:
                    controller = DiaryController()
                    controller.run()

                #check if de gebruiker game mode heeft gekozen voor hangman
                if string_to_int_casted_request == HANG_REQUEST:
                    controller = HangManController()
                    controller.run()



        except Exception as e:
            # Handles the exception
            print(f"An error occurred [handleRequest]: {e}")

    def run(self):
        try:
            game_started: bool = True
            self.printWelcomeMessage()

            while game_started:
                # get the user option
                mode_selected: int = input("")

                # check of de optie gekozen leeg is en of het geen getal is
                if mode_selected == "" or mode_selected.isnumeric() == False:
                    print("Kies een getaal en probeer het nogmals\n")

                # check of de optie gekozen niet leeg is en of het een getal is
                if mode_selected != "" and mode_selected.isnumeric() == True:
                    # print("keueze is " + mode_selected) TODO REMOVE

                    CLOSE_REQUEST: int = 10

                    # detect if option 10 is chosen is closed
                    string_to_int_casted_mode = int(mode_selected)
                    if string_to_int_casted_mode == CLOSE_REQUEST:
                        print("Nano store afgesloten")
                        break

                    self.handleRequest(mode_selected)
                    # end while loop TODO if we want to keep the game loop running remove break
                    # break
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [NanoXLController-run]: {e}")
