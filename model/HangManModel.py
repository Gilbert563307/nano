import json
import os
from helpers.Helpers import Helpers
from colorama import Fore
from config import config


class HangManModel:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def getHangManFileName(self) -> str:
        try:
            file_name: str = "hangmanwords.txt"
            return file_name
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManFileName]: {e}")

    def getHangManScoreFileName(self) -> str:
        try:
            file_name: str = "hangmanscore.txt"
            return file_name
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManScoreFileName]: {e}")

    def saveHangmanScoreToUser(self, name: str, score: int, won: bool) -> None:
        try:
            # Noteer in een tekstbestand de naam van de gebruiker, of de gebruiker het woord heeft geraden, het aantal keer raden en de datum
            file_name: str = self.getHangManScoreFilePath()

            # open file in append mode
            file = open(file_name, "a")

            # get win in dutch
            win_str: str = "Ja" if won else "Nee"

            #get todays date
            todays_date: str = self._getHelpersService().getTodaysDate()

            # genrate txt to write
            text_to_write: str = f"\n{name};woord geraden:{win_str};aantal keer:{score};datum:{todays_date}"

            # write to file
            file.write(text_to_write)

            # close file
            file.close()

        except Exception as e:
            print(f"An error occurred [saveHangmanScoreToUser]: {e}")

    def getHangManFilePath(self) -> str:
        try:
            # get current folder diir
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            # get file name
            file_name: str = self.getHangManFileName()

            # create file path
            file_path: str = f"{current_dir_path}\json\{file_name}"

            return file_path
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManFilePath]: {e}")
    
    def getHangManScoreFilePath(self) -> str:
        try:
            # get current folder diir
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            # get file name
            file_name: str = self.getHangManScoreFileName()

            # create file path
            file_path: str = f"{current_dir_path}\json\{file_name}"

            return file_path
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManScoreFilePath]: {e}")

    def getHangManWordsByDifficulty(self, difficulty=1) -> list[str]:
        try:
            # get file name
            file_name: str = self.getHangManFilePath()
            with open(file_name, "r") as file:
                content = file.read()

            # Split the content by commas, this will create a list of words
            words = content.split(",")

            # create temp words array
            words_array: list[str] = []

            #  Loop through each word in the list
            for item in words:
                # Strip any extra spaces or newlines around the word
                word = item.strip()

                word_len: int = len(word)

                # if  difficulty == easy
                if difficulty == config.EASY_WORDS_OPTION and word_len <= 5:
                    words_array.append(word)

                # if  difficulty == average
                if (
                    difficulty == config.AVERAGE_WORDS_OPTION
                    and word_len > 5
                    and word_len <= 10
                ):
                    words_array.append(word)

                # if  difficulty == HARD
                if difficulty == config.HARD_WORDS_OPTION and word_len > 10:
                    words_array.append(word)

            return words_array

        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManJsonFileNam]: {e}")

    def checkHangmanWordsFileExists(self) -> bool:
        try:
            # create file path
            file_path: str = self.getHangManFilePath()

            # check if the file exists
            file_exists = os.path.isfile(file_path)
            return file_exists
        except Exception as e:
            print(f"An error [checkHangmanWordsFileExists]: {e}")

    def checkHangmanWordsFileIsEmpty(self) -> bool:
        try:
            # get current folder diir
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            # get folder name
            file_name: str = self.getHangManFileName()

            # create file path
            file_path: str = f"{current_dir_path}\json\{file_name}"

            # open file in read mode
            with open(file_path, "r") as file_obj:

                # read first character
                first_char = file_obj.read(1)

                # if the json file exists but its empty
                if not first_char:
                    return True
            return False

        except Exception as e:
            print(f"An error [checkHangmanWordsFileIsEmpty]: {e}")

    def getHangManWords(self, difficulty=1) -> dict:
        try:
            # get file name
            file_name: str = self.getHangManFileName()
            # check if the file exists
            does_the_file_exist: bool = self.checkHangmanWordsFileExists()

            # if file does not exist
            if does_the_file_exist == False:
                message: str = (
                    f"Het bestand met de naam '{file_name}' kan niet worden gevonden in de map 'json'."
                )

                # return dict with info
                return {"words": [], " message": message, "error": True}

            # if file exists, check if file is emoty
            is_file_empty: bool = self.checkHangmanWordsFileIsEmpty()
            if is_file_empty:
                message = (
                    f"Het bestand '{file_name}' is leeg. Vul de woorden in volgens het volgende formaat:\n[\n"
                    "    {\n"
                    "        'makkelijke_woorden': [\n"
                    "            // Voeg hier de makkelijke woorden toe\n"
                    "        ]\n"
                    "    },\n"
                    "    {\n"
                    "        'gemiddelde_woorden': [\n"
                    "            // Voeg hier de gemiddelde woorden toe\n"
                    "        ]\n"
                    "    },\n"
                    "    {\n"
                    "        'moeilijke_woorden': [\n"
                    "            // Voeg hier de moeilijke woorden toe\n"
                    "        ]\n"
                    "    }\n"
                    "]"
                )
                return {"words": [], " message": message, "error": True}

            # if file exists and is not empty
            words: list[str] = self.getHangManWordsByDifficulty(difficulty)
            return {"words": words, " message": None, "error": None}

        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManWords]: {e}")
