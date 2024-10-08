import random
from typing import Dict, List
from helpers.Helpers import Helpers
from colorama import Fore
from config import config


class SudokuController:

    def __init__(self) -> None:
        self.grid_keys_location: list = []
        self.grid_rows: list = []
        self.grid_columns: list = []
        self.map: str = ""

    def setGridKeysLocation(self, grid_keys_location: list) -> bool:
        try:
            self.grid_keys_location = grid_keys_location
            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [setGridKeysLocation]: {e}")
            return False

    def getGridKeysLocation(self) -> list[Dict]:
        try:
            return self.grid_keys_location
        except Exception as e:
            print(f"An error occurred [getGridKeysLocation]: {e}")
            return []

    def setGridRows(self, grid_rows: list) -> bool:
        try:
            self.grid_rows = grid_rows
            return True
        except Exception as e:
            print(f"An error occurred [setGridRows]: {e}")
            return False

    def setGridColumns(self, grid_columns: list) -> bool:
        try:
            self.grid_columns = grid_columns
            return True
        except Exception as e:
            print(f"An error occurred [setGridColumns]: {e}")
            return False

    def setMap(self, map_data: str) -> bool:
        try:
            self.map = map_data
            return True
        except Exception as e:
            print(f"An error occurred [setMap]: {e}")
            return False

    def getMap(self) -> str:
        try:
            return self.map
        except Exception as e:
            print(f"An error occurred [getMap]: {e}")
            return ""

    def getAlfabet(self) -> list[str]:
        return ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def getGridColumns(self) -> list[int]:
        try:
            return self.grid_columns
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getGridColumns]: {e}")

    def getGridRows(self) -> list[int]:
        try:
            return self.grid_rows
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getGridRows]: {e}")

    def updateGameMap(self, updated_grid_rows: list[int]) -> bool:
        try:
            alfabet: List[str] = self.getAlfabet()

            grid_columns = [[] for _ in range(config.GRID_PATTERN)]

            for list in updated_grid_rows:
                for index in range(config.GRID_PATTERN):
                    first_item_of_each_list = list[index]
                    grid_columns[index].append(first_item_of_each_list)

            self.setGridColumns(grid_columns)
            self.setGridRows(updated_grid_rows)

            grid_map: str = self.createSudokuStringForUser(
                updated_grid_rows, alfabet)
            self.setMap(grid_map)

            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [updateGameMap]: {e}")

    def getUniqueGrid(self) -> list[int]:
        try:
            unique_columns_and_not_unique_rows = [
                [] for _ in range(config.GRID_PATTERN)]
            unique_rows_and_columns = [[] for _ in range(config.GRID_PATTERN)]

            grid_columns = [[] for _ in range(config.GRID_PATTERN)]

            for col in unique_columns_and_not_unique_rows:
                for index in range(config.GRID_PATTERN):
                    random_int = random.randint(0, 9)
                    # # create unqie column but not a row
                    random_bool = random.getrandbits(1)
                    if random_bool and random_int not in col:
                        col.append(random_int)
                    else:
                        col.append(0)

                    # turn each column into a unique row: else append 0
                    first_item_of_each_colum = col[index]

                    if first_item_of_each_colum not in unique_rows_and_columns[index]:
                        unique_rows_and_columns[index].append(
                            first_item_of_each_colum)
                    else:
                        unique_rows_and_columns[index].append(0)

            for list in unique_rows_and_columns:
                for index in range(config.GRID_PATTERN):
                    first_item_of_each_list = list[index]
                    grid_columns[index].append(first_item_of_each_list)

            # set rows and columns to global state
            self.setGridColumns(grid_columns)
            self.setGridRows(unique_rows_and_columns)

            return unique_rows_and_columns
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getUniqueGrid]: {e}")

    def createGridKeysAndLocation(self, rows: list) -> list[dict]:
        try:
            grid_keys_location: list = []
            row_count: int = 1
            alfabet = self.getAlfabet()
            for row in rows:
                for index in range(config.GRID_PATTERN):
                    item_of_each_column = row[index]
                    key = f"{alfabet[index]}"
                    key_location = {
                        "key": key,
                        "row": row_count,
                        "number": item_of_each_column,
                        "index": index,
                    }

                    grid_keys_location.append(key_location)
                row_count += 1

            return grid_keys_location
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [createGridKeysAndLocation]: {e}")

    def getColumnsAndHeaders(self) -> dict:
        try:
            rows: list[int] = self.getUniqueGrid()
            grid_keys_location: list[dict] = self.createGridKeysAndLocation(
                rows)

            self.setGridKeysLocation(grid_keys_location)
            return {"grid_keys_location": grid_keys_location, "grid": rows}
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getColumnsAndHeaders]: {e}")

    def createSudokuStringForUser(self, rows: list[int], alfabet: list[str]) -> str:
        try:
            # Define ANSI escape color codes bron: chatgpt needed colors highlter for each row
            colors = [
                "\033[91m",  # Red
                "\033[92m",  # Green
                "\033[93m",  # Yellow
                "\033[94m",  # Blue
                "\033[95m",  # Magenta
                "\033[96m",  # Cyan
                "\033[97m",  # White
                "\033[91m",  # Red
                "\033[92m",  # Green
                "\033[93m",  # Yellow
            ]
            reset_color = "\033[0m"

            view_to_print: str = " "
            for letter in alfabet:
                view_to_print += f"{letter}  "

            view_to_print += "\n"

            row_count: int = 0
            for row in rows:
                row_count += 1
                view_to_print += f"{colors[row_count]
                                    }{row} {reset_color}{row_count} \n"

            return view_to_print
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [createSudokuStringForUser]: {e}")

    def createSudokuMap(self) -> str:
        try:
            alfabet: list[str] = self.getAlfabet()
            data: dict = self.getColumnsAndHeaders()
            rows: list[int] = data.get("grid")

            view_to_print: str = self.createSudokuStringForUser(rows, alfabet)
            self.setMap(view_to_print)
            return view_to_print
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [createSudokuMap]: {e}")

    def updateGridKeyLocations(self, rows: list[int]) -> bool:
        try:
            grid_keys_location: list[dict] = self.createGridKeysAndLocation(
                rows)

            self.setGridKeysLocation(grid_keys_location)
            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [updateGridKeyLocations]: {e}")
            return False
        
    
    def checkIfUserHasWonGame(self) -> bool:
        try:
            grid_rows: list[int] = self.getGridRows()
            for row in grid_rows:
                if 0 in row:
                    return False
            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [checkIfUserHasWonGame]: {e}")
            return False

    def getKeyLocation(self, input) -> dict:
        try:
            # grid_key_locations: list[Dict] = self.updatedGridKeyLocations()
            grid_key_locations: list[Dict] = self.getGridKeysLocation()
            uppercase_str: str = input.upper()

            letter_to_find: str = uppercase_str[0]
            row_number_to_find: str = uppercase_str[1]

            for dict in grid_key_locations:
                key: str = dict.get("key")
                row: int = dict.get("row")

                if key == letter_to_find and str(row) == row_number_to_find:
                    # number: int | str = dict.get("number")  # find type TODO
                    return {"message": "", "error": False, "location": dict}

            return {"message": "", "error": False, "location": {}}
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [getKeyLocation]: {e}")

    def askUserForKeyGridLocation(self) -> dict:
        try:
            alfabet: list[str] = self.getAlfabet()

            while True:
                answer: str = input("Sleutel: ")

                if answer == "":
                    print("Vul een waarde in")

                if answer == "exit":  # TODO FINISH
                    return {"message": "", "error": False, "location": {}}

                anwser_length: int = len(answer)
                if anwser_length < 2 or anwser_length > 3:
                    print(
                        "Je waarde moet minstens er zo uit zien: [kollom]+[rij] bijv: A1"
                    )
                    return self.askUserForKeyGridLocation()

                if answer[0].upper() not in alfabet:
                    self._getHelpersService().printColouredMessage(
                        "Je waarde moet een kollom bevatten bijv: A1", Fore.YELLOW
                    )
                    return self.askUserForKeyGridLocation()

                if anwser_length >= 2:
                    if answer[1].isdigit() == False:
                        self._getHelpersService().printColouredMessage(
                            "Je waarde moet een getal bevatten bijv: A1", Fore.YELLOW
                        )
                        return self.askUserForKeyGridLocation()

                    # list of digits from 1 to 9
                    allowed_digits: list[int] = [num for num in range(1, 10)]

                    digit: None = None
                    if anwser_length == 2:
                        digit: int = int(answer[1])
                    elif anwser_length == 3:
                        digit: int = int(answer[1:3])

                    if digit != None and digit not in allowed_digits:
                        print("Je kollom kon niet worden gevonen")
                        return self.askUserForKeyGridLocation()

                    results: dict = self.getKeyLocation(answer)
                    if results["error"]:
                        self._getHelpersService().printColouredMessage(
                            results["error"], Fore.RED
                        )
                        # recursive
                        return self.askUserForKeyGridLocation()
                    else:
                        return results
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [askUserForKeyGridLocation]: {e}")

    def trySavingNumberToGrid(self, number_to_save: int, location: dict) -> dict:
        try:
            alfabet: list[str] = self.getAlfabet()

            column_key_to_check: int = alfabet.index(location.get("key"))
            row_key_to_check: int = location.get("row")

            all_grid_rows: list[int] = self.getGridRows()
            grid_row: list[int] = all_grid_rows[(row_key_to_check - 1)]

            grid_colum: list[int] = self.getGridColumns()[column_key_to_check]

            if number_to_save in grid_row or number_to_save in grid_colum:
                return {
                    "message": "Het getal mag niet in de rij en kollom zijn",
                    "error": True,
                    "grid_rows": [],
                }

            # get the index of the zero we want to replace by the number to save
            index: int = location.get("index")
            grid_row[index] = number_to_save

            # update all grid rows with newly updated grid row
            all_grid_rows[(row_key_to_check - 1)] = grid_row

            return {"message": "", "error": False, "grid_rows": all_grid_rows}
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [trySavingNumberToGrid]: {e}")

    def handleGameLogic(self) -> None:
        try:
            map: str = self.getMap()
            print(map)

            # check if the user has won
            user_won: bool = self.checkIfUserHasWonGame()
            if user_won:
                message: str = "Je heb gewonnen!!! \n"
                self._getHelpersService().printColouredMessage(message, Fore.GREEN)
                self._getHelpersService().printGameOptionsToUser(header=False)
                return

            results: dict = self.askUserForKeyGridLocation()
            location: dict = results.get("location")

            if len(location) == 0:
                # end game looop
                self._getHelpersService().printGameOptionsToUser(header=False, clear_console=True)
                return

            if location.get("number") != 0:
                message: str = "Deze locatie bevat al een waarde"
                print(message)
                return self.handleGameLogic()

            # ask user to save number to that location
            number_to_save: int = self.askUserForNumber()

            # check if number can be saved to that location'
            results: dict = self.trySavingNumberToGrid(
                number_to_save, location)
            if results["error"]:
                self._getHelpersService().printColouredMessage(
                    results["message"], Fore.RED
                )
                return self.handleGameLogic()

            updated: bool = self.updateGameMap(results["grid_rows"])
            if updated:
                return self.handleGameLogic()
            else:
                self._getHelpersService().printColouredMessage("Er iets fout gegaan", Fore.RED)

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [handleGameLogic]: {e}")

    def askUserForNumber(self) -> int:
        try:
            allowd_options: list[int] = [num for num in range(1, 10)]
            print("Voer hier het getal in dat je op deze locatie wilt plaatsen.")
            while True:
                number: str = input()

                if number == "":
                    message: str = "Je keuze mag niet leeg zijn.\n"
                    self._getHelpersService().printColouredMessage(message, Fore.RED)
                    continue

                if number.isnumeric() == False:
                    message: str = "Voer een geldig getal in.\n"
                    self._getHelpersService().printColouredMessage(message, Fore.RED)
                else:
                    casted_number: int = int(number)
                    if casted_number not in allowd_options:
                        message: str = "Voer een getal tussen 1-9 in. \n"
                        self._getHelpersService().printColouredMessage(
                            message, Fore.RED
                        )

                    if casted_number in allowd_options:
                        return casted_number

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [askUserForNumber]: {e}")

    def run(self):
        try:
            self.createSudokuMap()
            self.handleGameLogic()

        except Exception as e:
            # Handles the exception
            print(f"An error occurred [run]: {e}")
