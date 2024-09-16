# declare available optiopns
EASY_WORDS_OPTION: int = 1
AVERAGE_WORDS_OPTION: int = 2
HARD_WORDS_OPTION: int = 3

# list of available options
HANG_MAN_WORD_DIFFICULTY_OPTIONS: list[int] = [
    EASY_WORDS_OPTION,
    AVERAGE_WORDS_OPTION,
    HARD_WORDS_OPTION,
]

#when on diary option screen
CREATE_NEW_NOTE_TO_DIARY_OPTION: int = 1
READ_EXISTING_NOTE_TO_DIARY_OPTION: int = 2
UPDATE_EXISTING_NOTE_IN_DIARY_OPTION: int = 3
CREATE_NEW_NOTE_WITH_TODAYS_DATE_IN_DIARY_OPTION: int = 4
DIARY_GO_BACK_TO_MAIN_MENU: int = 5

# create array of allowed diary options
ALLOWED_DIARY_OPTIONS = [
    CREATE_NEW_NOTE_TO_DIARY_OPTION,
    READ_EXISTING_NOTE_TO_DIARY_OPTION,
    UPDATE_EXISTING_NOTE_IN_DIARY_OPTION,
    CREATE_NEW_NOTE_WITH_TODAYS_DATE_IN_DIARY_OPTION,
    DIARY_GO_BACK_TO_MAIN_MENU,
]

#NanoXLController configs
GUESS_THE_NUMBER_REQUEST: int = 1
DIARY_REQUEST: int = 2
HANG_REQUEST: int = 3
GUI_REQUEST: int = 4
CLOSE_REQUEST: int = 10

