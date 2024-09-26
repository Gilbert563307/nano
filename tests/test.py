import random


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
    json = {"column_one": [], "column_two": [], "column_three": []}

    for list in sudoku_list:
        for index_in_list in range(VALUES_IN_EACH_LIST):
            random_int = random.randint(0, 9)

            # creates each list with unique number
            if random_int not in list:
                # add numbers in each columns
                if index_in_list == 0 and random_int not in column_one:
                    column_one.append(random_int)
                    json["column_one"].append({index_in_list: random_int})
                    list[index_in_list] = random_int


                if index_in_list == 1 and random_int not in column_two:
                    column_two.append(random_int)
                    json["column_two"].append({index_in_list: random_int})
                    list[index_in_list] = random_int


                if index_in_list == 2 and random_int not in column_three:
                    column_three.append(random_int)
                    json["column_three"].append({index_in_list: random_int})
                    list[index_in_list] = random_int


              

    # print(f"col1 {column_one}")
    # print(f"col2 {column_two}")
    # print(f"col3 {column_three}")
    print(f"list {json}")

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


map = printSudokuMap()
print(map)

