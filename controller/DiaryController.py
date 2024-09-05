from helpers.Helpers import Helpers
from model.DiaryModel import DiaryModel
import os
from colorama import Fore, Style


class DiaryController:
    # initilianze
    def __init__(self):
        # self.diaryModel = None
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def _getDiaryModel(self) -> DiaryModel:
        return DiaryModel()

    def printDiaryAppOptions(self) -> None:
        print("Kies (1) om een nieuwe notitie op te slaan.")
        print("Kies (2) om een bestaande notitie te bekijken.")
        print("Kies (3) om terug naar de appstore te gaan.\n")

    def askUserForDiaryPassword(
        self,
    ):
        try:
            # create array of allowed passwords
            allowed_passwords = ["1234", "password", "utrecht"]

            print(
                "Vul het juiste wachtwoord in om toegang te krijgen tot het dagboek, je heb 3 pogingen: \n"
            )

            # times user can guess password
            number_of_times_user_can_guess: int = 3
            for times_to_guess in range(number_of_times_user_can_guess):
                user_typed_password: str = input("")

                is_pass_word_correct: (
                    bool
                ) = self._getDiaryModel().checkIfGivenPasswordValid(
                    user_typed_password, allowed_passwords
                )

                # check of the user gived password is correct
                if is_pass_word_correct == False:
                    print("Onjuiste wachtwoord probeer het nogmals\n")

                if is_pass_word_correct:
                    return True

            print("Onjuiste wachtwoord het dagboek wordt nu afgesloten.\n")
            self._getHelpersService().printGameOptionsToUser()  # TOO ASK IF NEEDED TO END GAME LOOP
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [askUserForDiaryPassword]: {e}")

    def run(self):
        try:
            # Dagboek
            # De requirements van het dagboek:
            # Voeg een wachtwoord toe aan het dagboek (check)
            # Vraag de gebruiker om welke dag het gaat (vandaag of een andere datum) (check)

            # Controleer of die datum nog vrij is(check)
            # Zo niet, vraag of de gebruiker tekst wilt toevoegen of dat de gebruiker tekst wilt herschrijven(check)
            # Vraag de gebruiker om een stuk tekst en voeg het toe aan het bestand dagboek.json/dagboek.csv (inclusief datum)

            # Geef de gebruiker de mogelijkheid om de tekst van een dag op te vragen en te lezen(TOD)
            # Geef de gebruiker de mogelijkheid om een tekst te bewerken(TODO)

            diary_opened = False

            # ask for the password
            has_user_access_to_diary = self.askUserForDiaryPassword()

            if has_user_access_to_diary:
                # set diary to opened true
                diary_opened: bool = True
                print("Successvol ingelod. \n ")
                print(
                   Fore.YELLOW + "In het dagboek kun je een nieuwe notitie opslaan of een bestaande log bewerken. \n"
                )
                self._getHelpersService().resetTerminalColour()

                self.printDiaryAppOptions()

                CREATE_NEW_NOTE_TO_DIARY_OPTION: int = 1
                READ_EXISTING_NOTE_TO_DIARY_OPTION: int = 2
                GO_BACK_TO_MAIN_MENU: int = 3

                # create array of allowed diary options
                allowed_diary_options = [
                    CREATE_NEW_NOTE_TO_DIARY_OPTION,
                    READ_EXISTING_NOTE_TO_DIARY_OPTION,
                    GO_BACK_TO_MAIN_MENU,
                ]

                mode: None
                while diary_opened:
                    diary_menu_option: str = input("")
                    # check if de gebruiker  zijn input niet leeg is en een integer bevat
                    is_user_input_valid = (
                        self._getHelpersService().checkIfUserInputIsAValidInt(
                            diary_menu_option
                        )
                    )

                    # check if user input is false
                    if is_user_input_valid == False:
                        print("Je keuze moet een getaal zijn")

                    # check if user option is false
                    if int(diary_menu_option) not in allowed_diary_options:
                        print(
                            "Je keuze moet een getaal tussen 1 en 3 zijn, probeer het nogmaals"
                        )

                    # check if user option is 1 or two then give access
                    if int(diary_menu_option) in allowed_diary_options:
                        mode = int(diary_menu_option)

                    # if user wants to go back to store
                    if mode == GO_BACK_TO_MAIN_MENU:
                        self._getHelpersService().printGameOptionsToUser(header=True)
                        break

                    # if all checks are done the code will break out the loop and call the next function
                    self.handleDiaryOptionMenuModeByGivenOption(mode)

                        # break
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [run]: {e}")

    def handleDiaryOptionMenuModeByGivenOption(self, mode: int):
        try:
            # create gamemode constants
            CREATE_NEW_NOTE_IN_DIARY_MODE: int = 1
            READ_EXISTING_NOTES_IN_DIARY_MODE: int = 2

            if mode == CREATE_NEW_NOTE_IN_DIARY_MODE:
                print("Voor welke datum wil je een notitie opslaan? \n")

                waiting_for_user_to_enter_date: bool = True

                while waiting_for_user_to_enter_date:
                    date_to_search: str = input(
                        "Voer de datum in het formaat dag/maand/jaar in:\n"
                    )
                    # checks  if the user inputed date is a valid string that has dag/maand/jaar format
                    is_gived_date_to_search_valid: (
                        bool
                    ) = self._getDiaryModel().checkIfTheSuggestedDateIsValid(
                        date_to_search
                    )
                    if is_gived_date_to_search_valid:
                        self.selfHandleDiaryNoteByGivenDate(date_to_search)
                        break

            if mode == READ_EXISTING_NOTES_IN_DIARY_MODE:
                print(
                    "Voor welke datum wil je de log bekijken? Gebruik het formaat dag/maand/jaar (bijv. 01/12/2024):\n"
                )

                waiting_for_user_to_enter_date: bool = True

                while waiting_for_user_to_enter_date:
                    # ask user for message
                    message_to_save: str = self.askUserForNote()

                    if message_to_save != "":
                        # check if the note is there
                        is_note_available_by_given_date: (
                            bool
                        ) = self._getDiaryModel().checkIfGivenDateIsExists(
                            message_to_save
                        )

                        if is_note_available_by_given_date == False:
                            print(
                                Fore.RED
                                + "Er is geen log gevonden voor je opgegeven datum \n"
                            )
                            self._getHelpersService().resetTerminalColour()
                            self.printDiaryAppOptions()
                            break

                        if is_note_available_by_given_date:
                            # fetch note log an return it
                            diary_log: str = self._getDiaryModel().getDiaryLogByDate(
                                message_to_save
                            )
                            print(f"Log: {diary_log} \n")
                            self.printDiaryAppOptions()
                            break

                    # check if there is a note by given date

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [run]: {e}")

    def promptUserToSaveDiaryNote(self, date: str) -> None:
        try:
            # print msg to user that there is no record in diary of given data
            print("Geen record gevonden voor de opgegeven datum.")
            print(
                f"Voer een waarde in; deze wordt onder de opegegeven {date}  datum opgeslagen.\n"
            )
            # ask user for message
            message_to_save: str = self.askUserForNote()

            # after message is recieverd
            if message_to_save != "":
                message_created: (
                    bool
                ) = self._getDiaryModel().createDiaryNoteByGivenDate(
                    date, message_to_save
                )

                if message_created == False:
                    # print message that note is saved
                    print(
                        "Jou notitie is niet opgeslagen in het dagboek, er is iets fout gegaan"
                    )

                if message_created:
                    # print message that note is saved
                    print("Jou notitie is opgeslagen in het dagboek \n")

                    # show options back to user
                    print("\n")
                    self.printDiaryAppOptions()

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [selfHandleDiaryNoteByGivenDate]: {e}")

    def selfHandleDiaryNoteByGivenDate(self, date_to_search: str) -> None:
        try:
            # check if diary file exists
            file_exists: bool = self._getDiaryModel().checkIfDiaryFileExists()

            # if diary file does not exists
            if file_exists == False:
                # create one first
                file_created: bool = self._getDiaryModel().createDiaryFile()
                self.promptUserToSaveDiaryNote(date_to_search)

            if file_exists:
                is_file_empty: bool = self._getDiaryModel().isDiaryFileEmpty()

                # als de file leeg is
                if is_file_empty:
                    self.promptUserToSaveDiaryNote(date_to_search)

                # als de file niet leeg is:
                if is_file_empty == False:

                    # search if the given date is free
                    is_given_date_available: (
                        bool
                    ) = self._getDiaryModel().checkIfGivenDateIsFreeInDiary(
                        date_to_search
                    )

                    # if the given date is free to use prompt user to save
                    if is_given_date_available:
                        self.promptUserToSaveDiaryNote(date_to_search)

                    if is_given_date_available == False:
                        self.promptUserToChooseOptionAfterNotAvaiableDateLog(
                            date_to_search
                        )


        except Exception as e:
            # Handles the exception
            print(f"An error occurred [selfHandleDiaryNoteByGivenDate]: {e}")

    def promptUserToOverrideExistingNote(self, date_to_overide: str) -> None:
        try:
            print(
                f"Voer een waarde in; deze wordt onder de opegegeven {date_to_overide}  datum opgeslagen.\n"
            )
            # ask user for message
            message_to_save: str = self.askUserForNote()

            # after message is recieverd
            if message_to_save != "":
                message_created: bool = self._getDiaryModel().updateDiaryNoteBy(
                    date_to_overide, message_to_save
                )

                if message_created == False:
                    print("Er is iets mis gegeaan met het wijzigen van je bericht.\n")

                if message_created:
                    print("Jou log is gewijzigd.\n")

                    #todo show options back to user TOO ADD OPTION 3
                    print("Kies (1) om een nieuwe notitie op te slaan.")
                    print("Kies (2) om een bestaande notitie te bekijken.\n")

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [promptUserToOverrideExistingNote]: {e}")

    def promptUserToChooseOptionAfterNotAvaiableDateLog(
        self, date_to_overide: str
    ) -> None:
        try:
            # if its not free then give user two options
            print("Er is al een log voor de opgegeven datum.\n")
            print("Wil je de huidige tekst overschrijven?\n")
            print("Kies (1) om te bevestigen, of (2) om te annuleren.")

            # define constant for options
            OVERRITE_EXISTING_LOG_OPTION: int = 1
            EXIT_OPTION: int = 2

            # set allowed options to choose froom
            allowed_options: list = [OVERRITE_EXISTING_LOG_OPTION, EXIT_OPTION]

            while True:
                chosen_option_todo: str = input("")

                # validae user input if its an integer
                is_user_input_valid: (
                    bool
                ) = self._getHelpersService().checkIfUserInputIsAValidInt(
                    chosen_option_todo
                )

                if is_user_input_valid == False:
                    print("Onjuiste keuze. Probeer het opnieuw.\n")

                # check if has not selected 1 or 2
                if int(chosen_option_todo) not in allowed_options:
                    print("Onjuiste keuze. Probeer het opnieuw.\n")

                # if user cancels
                if int(chosen_option_todo) == EXIT_OPTION:
                    print("Annulering \n")  # TODO finish remove
                    print("Kies (1) om een nieuwe notitie op te slaan.")
                    print("Kies (2) om een bestaande notitie te bekijken.\n")
                    break

                if int(chosen_option_todo) == OVERRITE_EXISTING_LOG_OPTION:
                    # TODO save new text
                    self.promptUserToOverrideExistingNote(date_to_overide)
                    break

        except Exception as e:
            # Handles the exception
            print(
                f"An error occurred [promptUserToChooseOptionAfterNotAvaiableDateLog]: {e}"
            )

    # this function will stay in the loop until the user has typed a messsage
    def askUserForNote(self) -> str:
        try:
            while True:
                # get user input
                message_to_save: str = input("")

                if message_to_save == "":
                    print("Vul een bericht in:\n")

                if message_to_save:
                    return message_to_save

        except Exception as e:
            # Handles the exception
            print(f"An error occurred: {e}")
