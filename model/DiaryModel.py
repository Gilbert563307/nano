import os
import json


class DiaryModel:
    # initilianze
    def __init__(self):
        pass

    def getDiaryJsonFileName(self) -> str:
        file_name: str = "dagboek.json"
        return file_name

    def checkIfGivenPasswordValid(self, password: str, valid_password: list) -> bool:
        if password not in valid_password:
            return False
        return True

    def checkIfDiaryFileExists(self) -> bool:
        try:
            # define file name
            file_name: str = self.getDiaryJsonFileName()

            # check if the file exists
            file_exists = os.path.isfile(file_name)
            return file_exists
        except Exception as e:
            # Handles the exception
            print(f"An error occurred: {e}")
            return False

    def createDiaryFile(self) -> bool:
        try:
            file_name: str = self.getDiaryJsonFileName()

            # create file,   x appends data to the end of the file
            file = open(file_name, "x")

            # close file
            file.close()
            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred: {e}")
            return False

    def updateDiaryNoteBy(self, date: str, message: str) -> bool:
        try:
            # get file name
            file_name: str = self.getDiaryJsonFileName()
            with open(file_name) as file:
                listObj = json.load(file)

            # loop through the data
            for item in listObj:
                date_from_json_data: str = item["date"]

                # if date is found
                if date_from_json_data == date:
                    # update the message
                    item["description"] = message
                    break

            # get file
            json_file = open(file_name, "w")
            json.dump(listObj, json_file, indent=4, separators=(",", ": "))

            # close file
            json_file.close()
            return True

        except Exception as e:
            # Handles the exception
            print(f"An error occurred: [updateDiaryNoteBy] {e}")
            return False
        
    def checkIfGivenDateIsExists(self, date: str) -> bool:
        try:
            # get file name
            file_name: str = self.getDiaryJsonFileName()
            with open(file_name) as file:
                listObj = json.load(file)
            
            # loop through the data
            for item in listObj:
                date_from_json_data: str = item["date"]

                # if date is found
                if date_from_json_data == date:
                    # return the message
                    return True
                
            return False
        except Exception as e:
            # Handles the exception
            print(f"An error occurred: [checkIfGivenDateIsExists] {e}")
            return False

    def createDiaryNoteByGivenDate(self, date: str, message_to_save: str) -> bool:
        try:
            # create json file                                      # adding this , makes it sure thet is will be placed in an array withing json objects
            json_value: list = ({"date": date, "description": message_to_save},)

            # get file name
            file_name: str = self.getDiaryJsonFileName()

            # check if file is empty
            is_json_file_empty: bool = self.isDiaryFileEmpty()

            if is_json_file_empty:
                # the json file to save the output data
                save_file = open(file_name, "w")
                json.dump(json_value, save_file, indent=6)

                # close file
                save_file.close()

            if is_json_file_empty == False:
                # Read JSON file
                with open(file_name) as file:
                    listObj = json.load(file)

                listObj.append(
                    {
                        "date": date,
                        "description": message_to_save,
                    }
                )

                # update list
                with open(file_name, "w") as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(",", ": "))

            return True
        except Exception as e:
            # Handles the exception
            print(f"An error occurred in [saveDiaryNoteToGivenDate]: {e}")
            return False

    def isDiaryFileEmpty(self) -> bool:
        try:
            # get file name
            file_name = self.getDiaryJsonFileName()
            # open file in read mode
            with open(file_name, "r") as file_obj:

                # read first character
                first_char = file_obj.read(1)

                # if the json file exists but its empty
                if not first_char:
                    return True
            return False
        except Exception as e:
            # Handles the exception
            print(f"An error occurred in [isDiaryFileEmpty]: {e}")

    def checkIfGivenDateIsFreeInDiary(self, date_to_check: str) -> bool:
        # get file name
        file_name = self.getDiaryJsonFileName()
        # open file name
        with open(file_name, "r") as file:
            jsonData = json.load(file)

        # loop through the data in the json file
        for item in jsonData:
            date_from_json_data: str = item["date"]
            # if date already exists
            if date_from_json_data == date_to_check:
                return False
        return True
    
    def getDiaryLogByDate(self, date: str) -> str:
        try:
            # get file name
            file_name = self.getDiaryJsonFileName()
            # open file name
            with open(file_name, "r") as file:
                jsonData = json.load(file)
            # loop through the data in the json file
            for item in jsonData:
                date_from_json_data: str = item["date"]
                # if date already exists
                if date_from_json_data == date:
                    return item["description"]
            return "Er is een geen log gevonden"
        except Exception as e:
            # Handles the exception
            print(f"An error occurred in [isDiaryFileEmpty]: {e}")
    
    def checkIfTheSuggestedDateIsValid(self, date_to_check: str) -> bool:
        allowed_string_lengths = [10, 9, 8]

        # check if date lenght is oke
        if len(date_to_check) not in allowed_string_lengths:
            return False

        # check if date contains  two slahes
        if date_to_check.count("/") != 2:
            return False

        return True
