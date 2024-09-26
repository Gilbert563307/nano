import random


rows = 6
sudoku_list = []

# for row in range(rows):

#     # vcerate empty list
#     empty_list = []
#     # append empty list
#     sudoku_list.append(empty_list)
#     row_list = sudoku_list[row]

    # for i in range(3):
    #     row_list = sudoku_list[row]

    #     random_int = random.randint(0, 9)

    #     if i == random.randint(0, 2):
    #         random_int = 0

    #     row_list.append(random_int)

    #     if row == 1:
    #         if random_int not in row_list:
    #             row_list.append(random_int)
    #     else:
    #         if random_int not in row_list and row_list != sudoku_list[len(sudoku_list) -1]:
    #             row_list.append(random_int)

    # # if is last row
    # if row == 5:
    #     if random_int not in row_list:
    #         for arr in sudoku_list:
    #             for num in arr:
    #                 if random_int != num:
    #                     row_list.append(random_int)


column_one = []
column_two = []
column_three = []
while len(column_one) < 6:
    random_int = random.randint(0, 9)
    if random_int not in column_one:
        column_one.append(random_int)

print(column_one)

