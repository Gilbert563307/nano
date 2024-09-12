# declare available optiopns
EASY_WORDS_OPTION: str = 1
AVERAGE_WORDS_OPTION: str = 2
HARD_WORDS_OPTION: str = 3

# list of available options
HANG_MAN_WORD_DIFFICULTY_OPTIONS: list[int] = [
    EASY_WORDS_OPTION,
    AVERAGE_WORDS_OPTION,
    HARD_WORDS_OPTION,
]

#when on diary option screen
CREATE_NEW_NOTE_TO_DIARY_OPTION: int = 1
READ_EXISTING_NOTE_TO_DIARY_OPTION: int = 2
UPDATE_EXISTING_NOTE: int = 3
DIARY_GO_BACK_TO_MAIN_MENU: int = 4

# create array of allowed diary options
ALLOWED_DIARY_OPTIONS = [
    CREATE_NEW_NOTE_TO_DIARY_OPTION,
    READ_EXISTING_NOTE_TO_DIARY_OPTION,
    UPDATE_EXISTING_NOTE,
    DIARY_GO_BACK_TO_MAIN_MENU,
]

#In diary game mode
CREATE_NEW_NOTE_IN_DIARY_MODE: int = 1
READ_EXISTING_NOTES_IN_DIARY_MODE: int = 2
