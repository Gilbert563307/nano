from helpers.Helpers import Helpers
from model.DiaryModel import DiaryModel
import os
from colorama import Fore
from config import config


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
        print(
            f"Kies ({config.CREATE_NEW_NOTE_TO_DIARY_OPTION}) om een nieuwe notitie op te slaan."
        )
        print(
            f"Kies ({config.READ_EXISTING_NOTE_TO_DIARY_OPTION}) om een bestaande notitie te bekijken."
        )
        print(
            f"Kies ({config.UPDATE_EXISTING_NOTE_IN_DIARY_OPTION}) om een notitie te bewerken"
        )
        print(
            f"Kies ({config.CREATE_NEW_NOTE_WITH_TODAYS_DATE_IN_DIARY_OPTION}) om een notitie aan te maken met de datum van vandaag.\n"
        )
        print(
            f"Kies ({config.DIARY_GO_BACK_TO_MAIN_MENU}) om terug naar de appstore te gaan.\n"
        )

    def askUserForDiaryPassword(
        self,
    ):
        try:
            # create array of allowed passwords
            allowed_passwords = ["1234", "password", "utrecht"]

            print(
                "Vul het juiste wachtwoord in om toegang te krijgen tot het dagboek, je heb 3 pogingen: (ww = 1234/password) \n"
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
            # Vraag de gebruiker om een stuk tekst en voeg het toe aan het bestand dagboek.json/dagboek.csv (inclusief datum)(check)

            # Geef de gebruiker de mogelijkheid om de tekst van een dag op te vragen en te lezen(check)
            # Geef de gebruiker de mogelijkheid om een tekst te bewerken(check)

            diary_opened = False

            # ask for the password
            has_user_access_to_diary = self.askUserForDiaryPassword()

            if has_user_access_to_diary:
                # set diary to opened true
                diary_opened: bool = True
                print("Successvol ingelod. \n ")
                print(
                    Fore.YELLOW
                    + "In het dagboek kun je een nieuwe notitie opslaan of een bestaande log bewerken. \n"
                )
                self._getHelpersService().resetTerminalColour()

                self.printDiaryAppOptions()

                allowed_diary_options: list[int] = config.ALLOWED_DIARY_OPTIONS

                while diary_opened:
                    # ask user for number, this while loop will not stop until the numer is gotten
                    diary_menu_option: int = (
                        self._getHelpersService().askUserForNumber()
                    )

                    # check if user option is false
                    if diary_menu_option not in allowed_diary_options:
                        print(
                            f"Je keuze moet een getaal tussen 1 en {len(allowed_diary_options)} zijn, probeer het nogmaals"
                        )

                    # if user wants to go back to store
                    if diary_menu_option == config.DIARY_GO_BACK_TO_MAIN_MENU:
                        self._getHelpersService().printGameOptionsToUser(header=True)
                        break

                    # check if user option is 1 or two then give access
                    if diary_menu_option in allowed_diary_options:
                        self.handleDiaryOptionMenuModeByGivenOption(diary_menu_option)

                # break
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [run]: {e}")

    def createNewNoteInDiary(self) -> None:
        try:
            print("Voor welke datum wil je een notitie opslaan? \n")

            waiting_for_user_to_enter_date: bool = True

            while waiting_for_user_to_enter_date:
                date_to_search: str = input(
                    "Voer de datum in het formaat dag/maand/jaar in (bijv. 01/12/2024):\n"
                )
                # checks  if the user inputed date is a valid string that has dag/maand/jaar format
                is_gived_date_to_search_valid: bool = (
                    self._getDiaryModel().checkIfTheSuggestedDateIsValid(date_to_search)
                )
                if is_gived_date_to_search_valid:
                    self.selfHandleDiaryNoteByGivenDate(date_to_search)
                    break
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [createNewNoteInDiary]: {e}")

    def createNewNoteWithTodaysDate(self) -> None:
        try:
            waiting_to_create_a_note: bool = True

            while waiting_to_create_a_note:
                date_to_create: str = self._getHelpersService().getTodaysDate()

                self.selfHandleDiaryNoteByGivenDate(date_to_create)
                break

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [createNewNoteWithTodaysDate]: {e}")

    def readNoteInDiary(self) -> None:
        try:
            print(
                "Voor welke datum wil je de log bekijken? Gebruik het formaat dag/maand/jaar (bijv. 01/12/2024):\n"
            )

            waiting_for_user_to_enter_date: bool = True

            while waiting_for_user_to_enter_date:
                # this code wil do a recursio when the message is not valid
                message_to_save: str = self.askUserForDateAndChechIfItsValid()

                if message_to_save:
                    # check if the note is there
                    is_note_available_by_given_date: bool = (
                        self._getDiaryModel().checkIfGivenDateIsExists(message_to_save)
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
                        self._getHelpersService().printColouredMessage(
                            f"Log: {diary_log} \n", Fore.GREEN
                        )
                        self.printDiaryAppOptions()
                        break
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [readNoteInDiary]: {e}")

    def updateNoteInDiary(self) -> None:
        try:
            # fetch all diary notes
            all_notes: list[str] = self._getDiaryModel().getAllNotes()

            # check for errors
            if all_notes["error"]:
                self._getHelpersService().printColouredMessage(
                    all_notes["message"], Fore.RED
                )

                self.printDiaryAppOptions()
                # end game loop
                return

            # if no there are no errors
            results: str = self.getNotesToDisplayText(all_notes["notes"])
            text_to_user: str = results["text_to_user"]

            # get the dates with the index number
            dates_linked_to_index: list[dict] = results["dates_linked_to_index"]

            # print notes to user
            self._getHelpersService().printColouredMessage(
                text_to_user, Fore.LIGHTCYAN_EX
            )

            # get all the correct indexes:
            index_list: list[int] = results["index_list"]

            # ask user for the index, this will loop until the user typed index in in the list
            index_to_search: int = self.askUserForIndexAndCheckIfItsTheList(index_list)

            # get date linked to that index
            date_to_update: str = next(
                item["date"]
                for item in dates_linked_to_index
                if item["index"] == index_to_search
            )

            # prompt user to overide log on that date
            self.promptUserToChooseOptionAfterNotAvaiableDateLog(date_to_update, False)
            return

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [updateNoteInDiary]: {e}")

    def handleDiaryOptionMenuModeByGivenOption(self, mode: int):
        try:
            if mode == config.CREATE_NEW_NOTE_TO_DIARY_OPTION:
                self.createNewNoteInDiary()

            if mode == config.READ_EXISTING_NOTE_TO_DIARY_OPTION:
                self.readNoteInDiary()

            if mode == config.UPDATE_EXISTING_NOTE_IN_DIARY_OPTION:
                self.updateNoteInDiary()

            if mode == config.CREATE_NEW_NOTE_WITH_TODAYS_DATE_IN_DIARY_OPTION:
                self.createNewNoteWithTodaysDate()

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [run]: {e}")

    def promptUserToSaveDiaryNote(self, date: str) -> None:
        try:
            # print msg to user that there is no record in diary of given data
            print("Geen record gevonden voor de opgegeven datum.")
            print(
                f"Voer een waarde in; deze wordt onder de opegegeven {date} datum opgeslagen.\n"
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
                    message: str = "Jou notitie is opgeslagen in het dagboek \n"
                    self._getHelpersService().printColouredMessage(message, Fore.GREEN)

                    # show options back to user
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
                f"Voer een waarde in; deze wordt onder de opegegeven {date_to_overide} datum opgeslagen.\n"
            )
            # ask user for message
            message_to_save: str = self.askUserForNote()

            # after message is recieverd
            if message_to_save != "":
                message_created: bool = self._getDiaryModel().updateDiaryNoteBy(
                    date_to_overide, message_to_save
                )

                if message_created == False:
                    self._getHelpersService().printColouredMessage(
                        "Er is iets mis gegeaan met het wijzigen van je bericht.\n",
                        Fore.RED,
                    )

                if message_created:
                    self._getHelpersService().printColouredMessage(
                        "Jou log is gewijzigd.\n", Fore.GREEN
                    )

                    # print home options to user
                    self.printDiaryAppOptions()

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [promptUserToOverrideExistingNote]: {e}")

    def promptUserToChooseOptionAfterNotAvaiableDateLog(
        self, date_to_overide: str, print_header_message: bool = True
    ) -> None:
        try:
            # if its not free then give user two options
            if print_header_message:
                print("Er is al een log voor de opgegeven datum.\n")
            print("Wil je de huidige tekst overschrijven?\n")
            print("Kies (1) om te bevestigen, of (2) om te annuleren.")

            # define constant for options
            OVERRITE_EXISTING_LOG_OPTION: int = 1
            EXIT_OPTION: int = 2

            # set allowed options to choose froom
            allowed_options: list = [OVERRITE_EXISTING_LOG_OPTION, EXIT_OPTION]

            while True:
                chosen_option_todo: int = self._getHelpersService().askUserForNumber()

                # check if has not selected 1 or 2
                if chosen_option_todo not in allowed_options:
                    print("Onjuiste keuze. Probeer het opnieuw.\n")

                # if user cancels
                if chosen_option_todo == EXIT_OPTION:
                    self._getHelpersService().printColouredMessage(
                        "Annulering \n", Fore.RED
                    )
                    self.printDiaryAppOptions()
                    break

                if chosen_option_todo == OVERRITE_EXISTING_LOG_OPTION:
                    # save new text
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
            print(f"An error occurred [askUserForNote]: {e}")

    def getNotesToDisplayText(self, notes: list[str]) -> dict:
        try:
            # create list that contains dict data to link index to a date
            dates_linked_to_index: list[dict] = []

            # create list to store only indexes int
            index_list: list[int] = []

            # create string to let user choose from
            text_to_user: str = ""

            # log messages to user
            self._getHelpersService().printColouredMessage(
                f"Alle notities:", Fore.LIGHTGREEN_EX
            )

            self._getHelpersService().printColouredMessage(
                "Selecteer een datum door het nummer van de gewenste optie in te vullen:",
                Fore.RED,
            )

            # create index count
            index = 0
            # loop through json data
            for note in notes:
                # increment index
                index += 1

                # push indexes into indexes list
                index_list.append(index)

                # create dict data, messages a linked to the index
                dict_data: dict = {"index": index, "date": note["date"]}
                dates_linked_to_index.append(dict_data)

                # create string to show to ther user
                text: str = (
                    f"[{index}]: Datum: {note['date']} Notitie: {note['description']} \n"
                )
                text_to_user += text

            return {
                "text_to_user": text_to_user,
                "dates_linked_to_index": dates_linked_to_index,
                "index_list": index_list,
            }

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getNotesToDisplayText]: {e}")

    def askUserForIndexAndCheckIfItsTheList(self, index_list: list[int]) -> int:
        try:
            # ask user for the index, this loop
            index_to_search: int = self._getHelpersService().askUserForNumber()

            # retun the index
            if index_to_search in index_list:
                return index_to_search

            if index_to_search not in index_list:
                text: str = ",".join(str(v) for v in index_list)
                self._getHelpersService().printColouredMessage(
                    f"Kies een getal tussen {text}", Fore.RED
                )
                # recoursion
                return self.askUserForIndexAndCheckIfItsTheList(index_list)

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [checkIfIndexIsInList]: {e}")

    def askUserForDateAndChechIfItsValid(self) -> str:
        try:
            # ask user for message

            message_to_save: str = self.askUserForNote()

            is_given_date_to_search_valid: bool = (
                self._getDiaryModel().checkIfTheSuggestedDateIsValid(message_to_save)
            )

            # if its valid
            if is_given_date_to_search_valid:
                return message_to_save

            # if its not valid send message to user and recall this function to get the message to save
            if is_given_date_to_search_valid == False:
                message: str = "Onjuiste datum probeer het nog een keer.\n"
                self._getHelpersService().printColouredMessage(message, Fore.RED)
                return self.askUserForDateAndChechIfItsValid()
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [askUserForDateAndChechIfItsValid]: {e}")
