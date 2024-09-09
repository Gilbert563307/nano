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

    def getHangManJsonFileName(self) -> str:
        try:
            file_name: str = "hangmanwords.json"
            return file_name
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManJsonFileName]: {e}")

    def getHangManJsonFilePath(self) -> str:
        try:
            # get current folder diir
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            # get folder name
            file_name: str = self.getHangManJsonFileName()

            # create file path
            file_path: str = f"{current_dir_path}\json\{file_name}"

            return file_path
        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManJsonFilePath]: {e}")

    def getHangManWordsByDifficulty(self, difficulty=1) -> list[str]:
        try:
            # get file name
            file_name: str = self.getHangManJsonFilePath()
            with open(file_name) as file:
                listObj = json.load(file)

            # loop through the data
            for item in listObj:
                # if  difficulty == easy
                if difficulty == config.EASY_WORDS_OPTION:
                    return item["makkelijke_woorden"]

                # if  difficulty == average
                if difficulty == config.AVERAGE_WORDS_OPTION:
                    return item["gemiddelde_woorden"]

                # if  difficulty == HARD
                if difficulty == config.HARD_WORDS_OPTION:
                    return item["moeilijke_woorden"]

        except Exception as e:
            # Handles the exception
            print(f"An error [getHangManJsonFileNam]: {e}")

    def checkHangmanWordsFileExists(self) -> bool:
        try:

            # create file path
            file_path: str = self.getHangManJsonFilePath()

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
            file_name: str = self.getHangManJsonFileName()

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
            file_name: str = self.getHangManJsonFileName()
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
