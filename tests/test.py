from datetime import date

def getTodaysDate() -> str:
    try:
        today = date.today()

        # get date in (ducth) day/month/year
        date_str: str = today.strftime("%d-%m-%Y")
        return date_str
    except Exception as e:
        print(f"An error occurred [getTodaysDate]: {e}")

test = getTodaysDate()
print(test)