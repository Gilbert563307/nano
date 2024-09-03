import random


class Nano:
    # initilianze
    def __init__(self):
        self.game_started: bool = True

    def printGameOptionsToUser(self):
        messages: list = [
            "Kies (1) voor Raad het getal?",
            "Kies (2) voor Voor je persoonlijke dagboek",
            "Kies (3) om het nano appstore af te sluiten\n",
        ]

        for message in messages:
            print(message)

    def printWelcomeMessage(self):
        print("Welkom bij  App Store op nano \n")
        print("Hier kan je een keuze maken voor welke type game je wilt spelen: \n")
        self.printGameOptionsToUser()

    def checkIfGameisRunning(self) -> bool:
        return self.game_started

    def getGameModeToPlay(self, gamemode: str):
        # check if gamemode is number
        if gamemode.isnumeric() == False:
            print("Vul een getaal in\n")

        # define game modes
        GUESS_THE_NUMBER_GAMEMODE = 1
        DIARY_GAMEMODE = 2

        # create array of allowed gamemodes
        allowed_gamemodes = [GUESS_THE_NUMBER_GAMEMODE, DIARY_GAMEMODE]

        # print("getGameModeToPlay line 21")
        string_to_int_casted_game_mode = int(gamemode)

        # check if user has not made right option between 1,2,3
        if string_to_int_casted_game_mode not in allowed_gamemodes:
            print("Onjuiste keuze probeer het nogmaals\n")

        # if user has made the right option
        if string_to_int_casted_game_mode in allowed_gamemodes:

            if string_to_int_casted_game_mode == GUESS_THE_NUMBER_GAMEMODE:
                self.randomNumberGuesser()

    def checkGuessedNumber(self, user_input: int, number_to_guess: int) -> bool:
        # check of de optie gekozen leeg is en of het geen getal is
        if user_input.isnumeric() == False:
            print("De ingevoerde waarde moet een getaal zijn\n")

        if user_input == "":
            print("Het veld mag niet leeg zijn\n")

        if int(user_input) == number_to_guess:
            return True
        return False

    def randomNumberGuesser(self):
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
        # remove one becuase the loop starts from 0, it will be six
        print(f"computer_generated_random_inter {computer_generated_random_inter}")

        # set variable to track is user has guessed the number correct, this is added for message tracking
        has_user_guessed_the_number: bool = False
        for times_to_guess in range(number_of_times_user_can_guess):

            # tell user how manu guesses he still has left
            times_to_guess_calculated = number_of_times_user_can_guess - times_to_guess
            print(f"Je heb nog {times_to_guess_calculated} pogingen.")

            guessed_number: int = input("Vul hier het getal in: \n")
            results = self.checkGuessedNumber(
                guessed_number, computer_generated_random_inter
            )

            # check if user has guessed the number correct
            if results == True:
                # set the tracking state to true
                has_user_guessed_the_number = True
                print("Je heb het getaal correct geraden!!!! ")
                # end foor loop then if user has guessed the number
                break

        # if the user has not guessed the number correct
        if has_user_guessed_the_number == False:
            print(f"Je heb het nummer niet geraden, \n")

        # closing meessage
        print(f"Het spel sluit zich nu af.\n")
        self.printGameOptionsToUser()

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
                    print("Nano store afgesloten")
                    break

                self.getGameModeToPlay(mode_selected)


app = Nano()
app.run()
