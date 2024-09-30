import random
import pprint
import string


VALUES_IN_EACH_LIST = 3


def createSudokuList() -> list:
    ROWS = 27
    # COLUMNS = 9
    sudoku_list = []

    for row_in_rows in range(ROWS):
        row_list = []
        for index_in_list in range(VALUES_IN_EACH_LIST):
            row_list.append(0)
        sudoku_list.append(row_list)

    return sudoku_list


def getSudokiListWithNumbers() -> list:
    sudoku_list = createSudokuList()
    column_one = []
    column_two = []
    column_three = []

    sudoku_list_arr_counter = 0

    rows = []

    for list in sudoku_list:
        random_int = random.randint(1, 9)

        for index_in_list in range(VALUES_IN_EACH_LIST):
            # creates each list with unique number

            if random_int not in list:
                # add numbers in each columns

                if index_in_list == 0 and random_int not in column_one:
                    column_one.append(random_int)
                    list[index_in_list] = random_int

                if index_in_list == 1 and random_int not in column_two:
                    column_two.append(random_int)
                    list[index_in_list] = random_int

                if index_in_list == 2 and random_int not in column_three:
                    column_three.append(random_int)
                    list[index_in_list] = random_int

        sudoku_list_arr_counter += 1
    # print(f" rows {rows}")

    return sudoku_list


def printSudokuMap():
    sudoku_list = getSudokiListWithNumbers()

    # this codes prints the map like is
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # ---------------------------
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # ---------------------------
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # [0, 0, 0][0, 0, 0][0, 0, 0]
    # ---------------------------

    str_to_pint = "\n"

    arr_index_counter = 0
    for list in sudoku_list:
        str_to_pint += str(list)
        arr_index_counter += 1

        # print list by 3 on each line
        if arr_index_counter % 3 == 0:
            str_to_pint += "\n"

        # print line after 9 lists are printed for readability
        if arr_index_counter % 9 == 0:
            str_to_pint += "---------------------------\n"

    return str_to_pint


# map = printSudokuMap()
# print(map)

ALFABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


def getColumnsAndHeaders() -> dict:
    columns = [[], [], [], [], [], [], [], [], []]
    rows = [[], [], [], [], [], [], [], [], []]

    for col in columns:
        for x in range(9):
            random_int = random.randint(0, 9)
            if random_int not in col:
                col.append(random_int)
            else:
                col.append(0)

    for col in columns:
        for index in range(9):
            first_item_of_each_colum = col[index]

            if first_item_of_each_colum not in rows[index]:
                rows[index].append(first_item_of_each_colum)
            else:
                rows[index].append(0)

    grid_keys_location = []
    row_count = 0
    for row in rows:
        for index in range(9):
            item_of_each_column = row[index]
            key = f"{ALFABET[index]}"
            key_location = {
                "key": key,
                "row": row_count,
                "number": item_of_each_column,
            }

            grid_keys_location.append(key_location)
        row_count += 1

    return {"grid_keys_location": grid_keys_location, "grid": rows}


def createSudokuMapVerTwo():
    data = getColumnsAndHeaders()
    to_print = " "
    for letter in ALFABET:
        to_print += f"{letter}  "

    to_print += "\n"
    rows = data.get("grid")

    row_count = 0
    for row in rows:
        row_count += 1
        to_print += f"{row} {row_count} \n"
    return to_print


test = createSudokuMapVerTwo()
print(test)
