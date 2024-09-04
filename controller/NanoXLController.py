from controller.RandomNumberGuesserController import RandomNumberGuesserController
from controller.DiaryController import DiaryController
from helpers.Helpers import Helpers

class NanoXLController:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def printWelcomeMessage(self):
        print("Welkom bij  App Store op nano \n")
        print("Hier kan je een keuze maken voor welke type game je wilt spelen: \n")
        self._getHelpersService().printGameOptionsToUser()

    def handleRequest(self, request: str):
        # check if gamemode is number
        if request.isnumeric() == False:
            print("Vul een getaal in\n")

        # define game modes
        GUESS_THE_NUMBER_REQUEST = 1
        DIARY_REQUEST = 2

        # create array of allowed gamemodes
        allowed_requests = [GUESS_THE_NUMBER_REQUEST, DIARY_REQUEST]

        # print("getGameModeToPlay line 21")
        string_to_int_casted_request = int(request)

        # check if user has not made right option between 1,2,3
        if string_to_int_casted_request not in allowed_requests:
            print("Onjuiste keuze probeer het nogmaals\n")

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


    def run(self):
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

                # detect if option 3 is chosen is closed
                string_to_int_casted_mode = int(mode_selected)
                if string_to_int_casted_mode == 3:
                    print("Nano store afgesloten")
                    break

                self.handleRequest(mode_selected)
                #end while loop TODO if we want to keep the game loop running remove break
                #break
