def getHangManWordsByDifficulty(self, difficulty=1) -> dict[str:[], str:str]:
    try:
        # create empty message
        message: str = ""

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

            # word length
            word_len: int = len(word)

            # list lentgh
            words_array_length: int = len(words_array)

            # if  difficulty == easy
            if difficulty == config.EASY_WORDS_OPTION:
                if word_len <= 5:
                    words_array.append(word)
                elif words_array_length == 0:
                    # if there are no easy words set message
                    message: str = (
                        "Er zijn geen woorden gevonden met precies 5 karakters."
                    )

            # if  difficulty == average
            if difficulty == config.AVERAGE_WORDS_OPTION:
                if word_len > 5 and word_len <= 10:
                    words_array.append(word)
                else:
                    print(f"words_array {words_array}")
                    if words_array_length == 0:
                        # if there are no average words set message
                        message: str = (
                            "Er zijn geen woorden gevonden met tussen de 5 en 10 karakters."
                        )

            # if  difficulty == hard
            if difficulty == config.HARD_WORDS_OPTION:
                if word_len > 10:
                    words_array.append(word)
                elif words_array_length == 0:
                    # if there are no hard words set message
                    message: str = (
                        "Er zijn geen woorden gevonden die meer dan 10 karakters bevatten."
                    )

        return {"words_array": words_array, "message": message}

    except Exception as e:
        # Handles the exception
        print(f"An error [getHangManJsonFileNam]: {e}")
