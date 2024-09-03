class Nano:
    # initilianze
    def __init__(self):
        self.game_started: bool = True

    def printWelcomeMessage(self):
        print("Welkom bij  App Store op nano \n")
        print("Hier kan je een keuze maken voor welke type game je wilt spelen: \n")
        print("Kies (1) voor Raad het getal?")
        print("Kies (2) voor Voor je persoonlijke dagboek")
        print("Kies (3) om het nano appstore af te sluiten\n")

    def checkIfGameisRunning(self) -> bool:
        return self.game_started

    def getGameModeToPlay(self, gamemode: str):
        # check if gamemode is number
        if gamemode.isnumeric() == False:
            print("Vul een getaal in\n")

        # create array of allowed gamemodes
        allowed_gamemodes = [1, 2, 3]

        # print("getGameModeToPlay line 21")
        string_to_int_casted_game_mode = int(gamemode)

        # check if user has not made right option between 1,2,3
        if string_to_int_casted_game_mode not in allowed_gamemodes:
            print("Onjuiste keuze probeer het nogmaals\n")

        # if user has made the right option
        if string_to_int_casted_game_mode in allowed_gamemodes:

            if string_to_int_casted_game_mode == 1:
                # randomNumberGuesser() TODO fix
                print("randomNumberGuesser FIX")

    def run(self):
        game_started: bool = self.checkIfGameisRunning()
        self.printWelcomeMessage()

        while game_started:
            # get the user option
            mode_selected: int = input("")

            # check of de optie gekozen leeg is en of het geen getal is
            if mode_selected == "" or mode_selected.isnumeric() == False:
                print("Kies een getaal en probeer het nogmals\n")

            # check of de optie gekozen niet leeg is en of het een getal is
            if mode_selected != "" and mode_selected.isnumeric() == True:
                # print("keueze is " + mode_selected) #TODO REMOVE

                # detect if option 3 is chosen is closed
                string_to_int_casted_mode = int(mode_selected)
                if string_to_int_casted_mode == 3:
                    print("Closing Nano store")
                    break

                self.getGameModeToPlay(mode_selected)


app = Nano()
app.run()
