from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, Frame
from helpers.Helpers import Helpers
from config import config
from model.WeatherModel import WeatherModel


class WeatherGuiController:

    # initilianze
    def __init__(self):
        self.frame = None
        self.canvas = None
        self.regio_text_field = None
        self.canvas_regio_item = None
        self.canvas_humidity_item = None
        self.canvas_wind_speed_item = None
        self.canvas_temp_item = None

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def _getWeatherModel(self) -> WeatherModel:
        try:
            return WeatherModel()
        except Exception as e:
            print(f"An error occurred [_getWeatherModel]: {e}")

    def relative_to_assets(self, file: str):
        try:
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            assets_path: str = (
                f"{current_dir_path}/builds/build_weather/build/assets/frame0"
            )
            return assets_path / Path(file)
        except Exception as e:
            print(f"An error occurred [relative_to_assets]: {e}")

    def getFrame(self) -> Frame:
        try:
            return self.frame
        except Exception as e:
            print(f"An error occurred [getFrame]: {e}")

    def setFrame(self, frame: Frame):
        try:
            self.frame = frame
        except Exception as e:
            print(f"An error occurred [setFrame]: {e}")

    def getCanvas(self) -> Canvas:
        try:
            return self.canvas
        except Exception as e:
            print(f"An error occurred [getCanvas]: {e}")

    def fetchWeather(self) -> None:
        try:
            place_to_search: str = self.regio_text_field.get()
            response: dict = self._getWeatherModel().fetchWeatherDataByParam(
                place_to_search
            )
            # get element of canvas_regio_item and change the text content
            self.getCanvas().itemconfig(self.canvas_regio_item, text=response["region"])
            self.getCanvas().itemconfig(
                self.canvas_humidity_item, text=response["humidity"]
            )
            self.getCanvas().itemconfig(
                self.canvas_wind_speed_item, text=response["wind_speed"]
            )
            self.getCanvas().itemconfig(self.canvas_temp_item, text=response["temp"])

        except Exception as e:
            print(f"An error occurred [fetchWeather]: {e}")

    def initUI(self) -> None:
        try:
            self.createCanvas()
            self.createHeader()
            self.createEntryImage()
            self.createInputField()
            self.createHr()

            # text fields
            self.createRegioTextFieldate()
            self.createHumidityTextField()
            self.createWindSpeedTextField()
            self.createTempTextField()

            # buttons
            self.createSearchButton()

        except Exception as e:
            print(f"An error occurred [initUI]: {e}")

    def createCanvas(self) -> None:
        try:
            frame: Frame = self.getFrame()
            canvas = Canvas(
                frame,
                bg="#FFFFFF",
                height=387,
                width=736,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )

            canvas.place(x=0, y=0)
            canvas.create_rectangle(0.0, 0.0, 736.0, 60.0, fill="#0E1E3D", outline="")

            # set canvas canavas
            self.canvas = canvas
        except Exception as e:
            print(f"An error occurred [createCanvas]: {e}")

    def createHeader(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas.create_text(
                255.0,
                7.0,
                anchor="nw",
                text="PocketApps",
                fill="#FFFFFF",
                font=("HachiMaruPop Regular", 32 * -1),
            )

        except Exception as e:
            print(f"An error occurred [createHeader]: {e}")

    def createEntryImage(self) -> None:
        try:
            frame: Frame = self.getFrame()

            # TODO check if needed

            # canvas: Canvas = self.getCanvas()

            # entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
            # entry_bg_1 = canvas.create_image(106.5, 160.5, image=entry_image_1)

            entry_1 = Entry(
                frame, bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0
            )
            entry_1.place(x=36.0, y=149.0, width=141.0, height=21.0)
            self.regio_text_field = entry_1

        except Exception as e:
            print(f"An error occurred [createEntryImage]: {e}")

    def createInputField(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas.create_text(
                36.0,
                131.0,
                anchor="nw",
                text="Plaats naam",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

        except Exception as e:
            print(f"An error occurred [createInputField]: {e}")

    def createHr(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas.create_rectangle(
                273.0, 108.0, 463.0, 255.0, fill="#D9D9D9", outline=""
            )

        except Exception as e:
            print(f"An error occurred [createHr]: {e}")

    def createRegioTextFieldate(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_regio_item = canvas.create_text(
                245.0,
                262.0,
                anchor="nw",
                text="Regio: ",
                fill="#000000",
                font=("Inter", 15 * -1),
            )
            self.canvas_regio_item = canvas_regio_item

        except Exception as e:
            print(f"An error occurred [createRegioTextFieldate]: {e}")

    def createHumidityTextField(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_humidity_item = canvas.create_text(
                113.0,
                262.0,
                anchor="nw",
                text="vochtigheid:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )
            self.canvas_humidity_item = canvas_humidity_item

        except Exception as e:
            print(f"An error occurred [createHumidityTextField]: {e}")

    def createWindSpeedTextField(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_wind_speed_item = canvas.create_text(
                522.0,
                258.0,
                anchor="nw",
                text="Wind snelheid:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            self.canvas_wind_speed_item = canvas_wind_speed_item

        except Exception as e:
            print(f"An error occurred [createWindSpeedTextField]: {e}")

    def createTempTextField(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_temp_item = canvas.create_text(
                385.0,
                262.0,
                anchor="nw",
                text="Temp:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            self.canvas_temp_item = canvas_temp_item

        except Exception as e:
            print(f"An error occurred [createTempTextField]: {e}")

    def createSearchButton(self) -> None:
        try:
            frame: Frame = self.getFrame()
            button_1 = Button(
                frame,
                text="Zoeken",
                borderwidth=0,
                highlightthickness=0,
                command=self.fetchWeather,
                relief="flat",
            )
            button_1.place(x=38.0, y=186.0, width=65.0, height=21.0)

        except Exception as e:
            print(f"An error occurred [createSearchButton]: {e}")

    def run(self, frame: Frame) -> None:
        try:
            self.setFrame(frame)
            self.initUI()
            self._getHelpersService().printGameOptionsToUser(header=True, clear_console=True)
        except Exception as e:
            print(f"An error occurred [run]: {e}")
