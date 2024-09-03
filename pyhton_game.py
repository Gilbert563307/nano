import random

game_started: bool = True


def printWelcomeMessage():
    print("Welkom bij  App Store op nano \n")
    print("Hier kan je een keuze maken voor welke type game je wilt spelen: \n")
    print("Kies (1) voor Raad het getal?\n")
    print("Kies (2) voor Voor je persoonlijke dagboek\n")
    print("Kies (3) om het nano appstore af te sluiten\n")


def getGameModeToPlay(gamemode: str):
    # check if gamemode is number
    if gamemode.isnumeric() == False:
        print("Vul een getaal in\n")

    # create array of allowed gamemodes
    allowed_gamemodes = [1, 2, 3]

    # print("getGameModeToPlay line 21")
    string_to_int_casted_game_mode = int(gamemode)

    # check if user has not made right option between 1,2,3
    if string_to_int_casted_game_mode not in allowed_gamemodes:
        print("Onjuiste keuze probeer het nogmaals\n")

    # if user has made the right option
    if string_to_int_casted_game_mode in allowed_gamemodes:

        if string_to_int_casted_game_mode == 1:
            randomNumberGuesser()


def checkGuessedNumber(user_input: int, number_to_guess: int) -> bool:
    # check of de optie gekozen leeg is en of het geen getal is
    if user_input.isnumeric() == False:
        print("Vul een getaal in\n")

    if user_input == "":
        print("Het veld mag niet leeg zijn\n")

    if int(user_input) == number_to_guess:
        return True
    return False


def randomNumberGuesser():
    # rand om getaal.
    # Laat de computer een random integer bepalen. (check)
    # Bepaal hoe vaak de gebruiker mag raden en hoe hoog het getal maximaal mag zijn. (check)
    # Gebruik een for-loop om de gebruiker een x-aantal keer te laten raden.
    # Communiceer aan de gebruiker hoe vaak de gebruiker mag raden en of het getal al wel of niet geraden is.

    lowest_guessable_number: int = 0
    highest_guessable_number: int = 15

    # random number between 0,15 both included
    print(
        f"Raad het getaal tussen de {lowest_guessable_number} en {highest_guessable_number} \n"
    )

    computer_generated_random_inter: int = random.randint(
        lowest_guessable_number, highest_guessable_number
    )

    # times user can guess
    number_of_times_user_can_guess: int = 5
    print(f"Je krijgt 5 pogingen \n")
    # remove one becuase the loop starts from 0, it will be six
    for times_to_guess in range((number_of_times_user_can_guess - 1)):
        guessed_number: int = input("")
        results = checkGuessedNumber(guessed_number, computer_generated_random_inter)


# print de options to the commandline
printWelcomeMessage()

while game_started:
    # get the user option
    mode_selected: int = input("")

    # check of de optie gekozen leeg is en of het geen getal is
    if mode_selected == "" or mode_selected.isnumeric() == False:
        print("Kies een getaal en probeer het nogmals\n")

    # check of de optie gekozen niet leeg is en of het een getal is
    if mode_selected != "" and mode_selected.isnumeric() == True:
        # print("keueze is " + mode_selected) TODO REMOVE
        getGameModeToPlay(mode_selected)
