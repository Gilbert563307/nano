import random
from datetime import date
import os
import json


class NanoXL:
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

    def getDiaryJsonFileName(self) -> str:
        file_name: str = "dagboek.json"
        return file_name

    def checkIfUserInputIsAValidInt(self, user_input: str) -> bool:
        # only checks if  input is not empty
        if user_input == "":
            return False

        # only checks if its a integer
        if user_input.isnumeric() == False:
            return False

        return True

    def checkIfTheSuggestedDateIsValid(self, date_to_check: str) -> bool:
        allowed_string_lengths = [10, 9, 8]

        # check if date lenght is oke
        if len(date_to_check) not in allowed_string_lengths:
            return False

        # check if date contains  two slahes
        if date_to_check.count("/") != 2:
            return False

        return True

    def setGameModeToPlay(self, gamemode: str):
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

            # check of de gebruiker de game mode heeft geozen voor raad het getaal
            if string_to_int_casted_game_mode == GUESS_THE_NUMBER_GAMEMODE:
                self.randomNumberGuesser()

            # check of de gebruiker de game mode heeft gekozen voor het dagboek
            if string_to_int_casted_game_mode == DIARY_GAMEMODE:
                self.openDiary()

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

    def askUserForDiaryPassword(
        self,
    ):
        # create array of allowed passwords
        allowed_passwords = ["1234", "password", "utrecht"]

        print(
            "Vul het juiste wachtwoord in om toegang te krijgen tot het dagboek, je heb 3 pogingen: \n"
        )

        # times user can guess password
        number_of_times_user_can_guess: int = 3
        for times_to_guess in range(number_of_times_user_can_guess):
            user_typed_password: str = input("")

            # check of the user gived password is correct
            if user_typed_password not in allowed_passwords:
                print("Onjuiste wachtwoord probeer het nogmals\n")

            if user_typed_password in allowed_passwords:
                return True

        print("Onjuiste wachtwoord het dagboek wordt nu afgesloten.\n")
        self.printGameOptionsToUser()

    def openDiary(self):
        # Dagboek
        # De requirements van het dagboek:
        # Voeg een wachtwoord toe aan het dagboek (check)
        # Vraag de gebruiker om welke dag het gaat (vandaag of een andere datum) (check)

        # Controleer of die datum nog vrij is
        # Zo niet, vraag of de gebruiker tekst wilt toevoegen of dat de gebruiker tekst wilt herschrijven
        # Vraag de gebruiker om een stuk tekst en voeg het toe aan het bestand dagboek.json/dagboek.csv (inclusief datum)

        # Geef de gebruiker de mogelijkheid om de tekst van een dag op te vragen en te lezen
        # Geef de gebruiker de mogelijkheid om een tekst te bewerken

        diary_opened = False

        # ask for the password
        has_user_access_to_diary = self.askUserForDiaryPassword()

        if has_user_access_to_diary:
            # set diary to opened true
            diary_opened = True
            print("Successvol ingelod. \n ")
            print(
                "In het dagboek kun je een nieuwe notitie opslaan of een bestaande log bewerken."
            )

            print("Kies (1) om een nieuwe notitie op te slaan.")
            print("Kies (2) om een bestaande notitie te bekijken.\n")

            # create array of allowed diary options
            allowed_diary_options = [1, 2]

            mode: None
            while diary_opened:
                diary_menu_option: str = input("")
                # check if de gebruiker  zijn input niet leeg is en een integer bevat
                is_user_input_valid = self.checkIfUserInputIsAValidInt(
                    diary_menu_option
                )

                # check if user input is false
                if is_user_input_valid == False:
                    print(
                        "Je keuze moet een getaal tussen 1 en 3 zijn, probeer het nogmaals"
                    )

                # check if user option is false
                if int(diary_menu_option) not in allowed_diary_options:
                    print(
                        "Je keuze moet een getaal tussen 1 en 3 zijn, probeer het nogmaals"
                    )

                # check if user option is 1 or two then give access
                if int(diary_menu_option) in allowed_diary_options:
                    mode = int(diary_menu_option)
                    # if all checks are done the code will break out the loop and call the next function
                    break

            self.showDiaryModeByGivenOption(mode)

    def showDiaryModeByGivenOption(self, mode: int):
        # create gamemode constants
        CREATE_NEW_NOTE_IN_DIARY_MODE: int = 1
        READ_EXISTING_NOTES_IN_DIARY_MODE: int = 2

        if mode == CREATE_NEW_NOTE_IN_DIARY_MODE:
            print("Voor welke datum wil je een notitie opslaan? \n")

            while True:
                date_to_search: str = input(
                    "Voer de datum in het formaat dag/maand/jaar in:\n"
                )

                is_gived_date_to_search_valid = self.checkIfTheSuggestedDateIsValid(
                    date_to_search
                )
                if is_gived_date_to_search_valid:
                    self.selfHandleDiaryNoteByGivenDate(date_to_search)
                    break

    def selfHandleDiaryNoteByGivenDate(self, date_to_search: str) -> None:
        try:
            # define file name
            file_name: str = self.getDiaryJsonFileName()

            # check if the file exists
            file_exists = os.path.isfile(file_name)

            # if file does not exists
            if file_exists == False:
                # create file
                file = open(file_name, "x")

                # print msg to user that there is no record in diary of given data
                print("Geen record gevonden voor de opgegeven datum.")
                print(
                    f"Voer een waarde in; deze wordt onder de opegegeven-{date_to_search}  datum opgeslagen.\n"
                )
                # load function to save data by input
                self.saveDiaryNoteToGivenDate(date_to_search)

            # if file exists
            if file_exists:
                # open file in read mode
                with open(file_name, "r") as file_obj:

                    # read first character
                    first_char = file_obj.read(1)

                    # if the json file exists but its empty
                    if not first_char:
                        print("Geen record gevonden voor de opgegeven datum.")
                        print(
                            f"Voer een waarde in; deze wordt onder de opegegeven-{date_to_search} datum opgeslagen.\n"
                        )
                        self.saveDiaryNoteToGivenDate(date_to_search)

                    # if file is not empty check if the given date is free
                    else:
                        # search if tje given date is free
                        is_given_date_available: bool = (
                            self.checkIfGivenDateIsFreeInDiary(date_to_search)
                        )

                        # if its not free then give user two options
                        if is_given_date_available == False:
                            print("Er is al een log voor de opgegeven datum.\n")
                            print("Wil je de huidige tekst overschrijven?\n")
                            print("Kies (1) om te bevestigen, of (2) om te annuleren.")

                            #define constant for options
                            EXIT_OPTION: int = 2
                            OVERRITE_EXISTING_LOG_OPTION: int = 1

                            # set allowed options to choose froom
                            allowed_options: list[OVERRITE_EXISTING_LOG_OPTION, EXIT_OPTION]

                            while True:
                                chosen_option_todo: str = input("")

                                # validae user input if its an integer
                                is_user_input_valid: bool = (
                                    self.checkIfUserInputIsAValidInt(chosen_option_todo)
                                )

                                if is_user_input_valid == False:
                                    print("Onjuiste keuze. Probeer het opnieuw.\n")

                                # check if has not selected 1 or 2
                                if int(chosen_option_todo) not in allowed_options:
                                    print("Onjuiste keuze. Probeer het opnieuw.\n")

                                # if user cancels
                                if int(chosen_option_todo) == EXIT_OPTION:
                                    print("Annulering")#TODO finis
                                    # self.printGameOptionsToUser()
                                    break

                                if int(chosen_option_todo) == OVERRITE_EXISTING_LOG_OPTION:
                                    # TODO save new text
                                    pass

        except Exception as e:
            # Handles the exception
            print(f"An error occurred: {e}")

    def saveDiaryNoteToGivenDate(self, date: str) -> None:
        try:
            # get user input
            message_to_save: str = input("")

            # create json file                                      # adding this , makes it sure thet is will be placed in an array withing json objects
            json_value = ({"date": date, "description": message_to_save},)

            # get file name
            file_name = self.getDiaryJsonFileName()

            # the json file to save the output data
            save_file = open(file_name, "w")
            json.dump(json_value, save_file, indent=6)

            # close file
            save_file.close()

            # print message that note is saved
            print("Jou notitie is opgeslagen in het dagboek")

        except Exception as e:
            # Handles the exception
            print(f"An error occurred in [saveDiaryNoteToGivenDate]: {e}")

    def getCurrenDateInDutchFormat(self) -> str:
        # creating the date object of today's date
        todays_date = date.today()

        todays_day = todays_date.day
        todays_month = todays_date.month
        todays_year = todays_date.year
        return f"{todays_day}/{todays_month}/{todays_year}"

    def checkIfGivenDateIsFreeInDiary(self, date_to_check: str) -> bool:
        # get file name
        file_name = self.getDiaryJsonFileName()
        # open file name
        with open(file_name, "r") as file:
            jsonData = json.load(file)

        # loop through the data in the json file
        for item in jsonData:
            date_from_json_data: str = item["date"]
            # if date already exists
            if date_from_json_data == date_to_check:
                return False
        return True

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

                self.setGameModeToPlay(mode_selected)


app = NanoXL()
app.run()
