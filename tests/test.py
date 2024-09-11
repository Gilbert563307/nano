indexes = []
text = "meerdere"

text_listed = list(text)

occurence_char = "e"

all_occurences = text.count(occurence_char)

count = -1
for char in text_listed:
    count += 1
    if char == occurence_char:
        indexes.append(count)
        print(f"location {count}: char {char}")


for index in indexes:
    text_listed[index] = "_"

print("".join(text_listed))


#  new_correct_gussed_chars: list[dict] = []

#             pos = 0
#             for char in word_to_guess:
#                 pos += 1
#                 data = {"pos": pos, "char": char}
#                 test_dict.append(data)



def getGameStats(
        self, word_to_guess: str, user_inputted_character, all_ready_guessed_chars
    ) -> dict:
        try:

            print(f"all_ready_guessed_chars {all_ready_guessed_chars}")
            # create the underscores to show to ther user
            keybaord_len_word: str = ""

            # set the _undercores for how many chars are in the word
            for char in word_to_guess:
                keybaord_len_word += "_"

            # create a list from the keybaord_len_word other wise we cant change the pos of that word
            list_keybaord_len_word = list(keybaord_len_word)

            # create a list from thr word to guess so that we can get the pos of the char
            list_word_to_guess = list(word_to_guess)

            # check if the occurence of the string is more than onece
            string_occurence_in_word_to_guess: int = word_to_guess.count(
                user_inputted_character
            )

            # if the user has inputted a letter that occurs more than once in  the word to guess
            if string_occurence_in_word_to_guess > 1:
                # all_occurences_locations: list[int] = []

                # set location_counter
                position = -1
                for char in word_to_guess:
                    position += 1
                    if char == user_inputted_character:
                        # all_occurences_locations.append(position)

                        # replace that underscore with the charater
                        list_keybaord_len_word[position] = f"{char}"
            else:
                # loop through each character of the word
                for char in word_to_guess:

                    if user_inputted_character in word_to_guess:
                        # get the position of the char in the word
                        position: int = list_word_to_guess.index(
                            user_inputted_character
                        )

                        # go to the list of the underscores, get the position of which underscore we want to replace
                        list_keybaord_len_word[position] = f"{user_inputted_character}"

            # loop through all the characters the user has already guessed
            for char in all_ready_guessed_chars:

                # check if char is not one of the occurrence characters
                if string_occurence_in_word_to_guess == 1:
                    # get the pos of the char that is in the created list of thr word to guess
                    position: int = list_word_to_guess.index(char)
                    # replace that underscore with the character
                    list_keybaord_len_word[position] = f"{char}"

            # join that list together and print thr word
            joined_list_word = " ".join(list_keybaord_len_word)

            # create message
            message: str = f"Woord: {joined_list_word} \n"
            return {"word": "".join(list_keybaord_len_word), "message": message}

        except Exception as e:
            print(f"An error occurred [printGameStats]: {e}")