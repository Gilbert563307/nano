from helpers.Helpers import Helpers
import requests


class WeatherModel:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def getApiKey(self) -> str:
        try:
            return self._getHelpersService().getEnvVar("WEATHER_API_KEY")
        except Exception as e:
            # Handles the exception
            print(f"An error [getApiKey]: {e}")

    def fetchWeatherDataByParam(self, param: str) -> dict:
        try:
            api_key: str = self.getApiKey()
            url: str = (
                f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={param}"
            )

            # fetch
            request = requests.get(url)
            response = request.json()

            data: dict = {}
            if response.get("error"):
                return {
                    "region": "NULL",
                    "temp": "NULL",
                    "wind_speed": "NULL",
                    "humidity": "NULL",
                }

            # return only the date we want to use
            data["region"] = f"Regio: {response['location']['region']}"

            data["temp"] = f"Temp: { response['current']['temp_c'] }"
            data["wind_speed"] = f"Wind snelheid: {response['current']['wind_kph']}"
            data["humidity"] = f"Vochtigheid: {response['current']['humidity']}"
            return data

        except Exception as e:
            # Handles the exception
            print(f"An error [fetchWeatherDataByParam]: {e}")
