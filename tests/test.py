import random
import pprint
import string


class SudokuController:

    def __init__(self) -> None:
        self.grid_keys_location = []
        self.grid_rows: list = []
        self.grid_columns: list = []

    def getAlfabet(self) -> list[str]:
        return ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def getUniqueGrid(self) -> list[int]:
        unique_columns_and_not_unique_rows = [[] for _ in range(9)]
        unique_rows_and_columns = [[] for _ in range(9)]

        grid_columns = [[] for _ in range(9)]

        for col in unique_columns_and_not_unique_rows:
            for index in range(9):
                random_int = random.randint(0, 9)
                # # create unqie column but not a row
                if random_int not in col:
                    col.append(random_int)
                else:
                    col.append(0)

                # turn each column into a unique row: else append 0
                first_item_of_each_colum = col[index]

                if first_item_of_each_colum not in unique_rows_and_columns[index]:
                    unique_rows_and_columns[index].append(first_item_of_each_colum)
                else:
                    unique_rows_and_columns[index].append(0)

        for list in unique_rows_and_columns:
            for index in range(9):
                first_item_of_each_list = list[index]
                grid_columns[index].append(first_item_of_each_list)

        # set rows and columns to global state
        self.grid_columns = grid_columns
        self.grid_rows = unique_rows_and_columns

        return unique_rows_and_columns

    def getGridKeysAndLocation(self, rows: list) -> dict:
        grid_keys_location: list = []
        row_count: int = 1
        alfabet = self.getAlfabet()
        for row in rows:
            for index in range(9):
                item_of_each_column = row[index]
                key = f"{alfabet[index]}"
                key_location = {
                    "key": key,
                    "row": row_count,
                    "number": item_of_each_column,
                }

                grid_keys_location.append(key_location)
            row_count += 1

        return grid_keys_location

    def getColumnsAndHeaders(self) -> dict:
        rows = self.getUniqueGrid()
        grid_keys_location = self.getGridKeysAndLocation(rows)

        self.grid_keys_location = grid_keys_location
        return {"grid_keys_location": grid_keys_location, "grid": rows}

    def createSudokuMap(self):
        alfabet = self.getAlfabet()
        data = self.getColumnsAndHeaders()
        view_to_print = " "
        for letter in alfabet:
            view_to_print += f"{letter}  "

        view_to_print += "\n"
        rows = data.get("grid")

        row_count = 0
        for row in rows:
            row_count += 1
            view_to_print += f"{row} {row_count} \n"
        return view_to_print

    def getKeyLocation(self, input):
        grid_key_locations = self.grid_keys_location
        uppercase_str = input.upper()

        letter_to_find = uppercase_str[0]
        row_number_to_find = uppercase_str[1]

        for dict in grid_key_locations:
            key = dict.get("key")
            row = dict.get("row")

            # print(f"dict {dict}  letter_to_find {letter_to_find} row_number_to_find {row_number_to_find} ley {key} row {row}")

            if key == letter_to_find and str(row) == row_number_to_find:
                number = dict.get("number")
                return {"message": "", "error": False, "location": dict}

        return {"message": "", "error": False, "location": {}}

    def askUserForKeyGridLocation(self) -> dict:

        while True:
            answer: str = input("Key: \n")

            if answer == "":
                print("Vul een waarde in")

            if len(answer) < 2 or len(answer) > 2:
                print("Je waarde moet minstens er zo uit zien: bijv[column]+[rij] A1")
            else:
                if answer:
                    results: dict  = self.getKeyLocation(answer)
                    if results["error"]:
                        print(results["error"])
                        #recursive
                        self.askUserForKeyGridLocation()
                    else:                    
                        return results

    def run(self):
        map = self.createSudokuMap()
        print(f"{map}")

        results: dict = self.askUserForKeyGridLocation()
        print(f"results {results}")

        # print(f"rows {self.grid_rows}")
        # print(f"grid_columns {self.grid_columns}")


run = SudokuController()
run.run()
