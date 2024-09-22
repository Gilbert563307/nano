from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
from helpers.Helpers import Helpers
from config import config

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\ssemp\Documents\MYHU\PROG\nano\builds\build_weather\build\assets\frame0"
)


class WeatherGuiController:

    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def relative_to_assets(self, path: str):
        return self._getHelpersService().relativeToAssets(ASSETS_PATH, path)

    def fetchWeather() -> None:
        try:
            pass
        except Exception as e:
            print(f"An error occurred [fetchWeather]: {e}")

    def run(self, Frame: Frame) -> None:
        try:
            canvas = Canvas(
                Frame,
                bg="#FFFFFF",
                height=387,
                width=736,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )

            canvas.place(x=0, y=0)
            canvas.create_rectangle(0.0, 0.0, 736.0, 60.0, fill="#0E1E3D", outline="")

            canvas.create_text(
                255.0,
                7.0,
                anchor="nw",
                text="PocketApps",
                fill="#FFFFFF",
                font=("HachiMaruPop Regular", 32 * -1),
            )

            canvas.create_text(
                36.0,
                131.0,
                anchor="nw",
                text="Plaats naam",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
            entry_bg_1 = canvas.create_image(106.5, 160.5, image=entry_image_1)
            entry_1 = Entry(
                Frame, bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0
            )
            entry_1.place(x=36.0, y=149.0, width=141.0, height=21.0)

            canvas.create_rectangle(
                273.0, 108.0, 463.0, 255.0, fill="#D9D9D9", outline=""
            )

            canvas.create_text(
                273.0,
                262.0,
                anchor="nw",
                text="Regio: ",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            canvas.create_text(
                113.0,
                262.0,
                anchor="nw",
                text="vochtigheid:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            canvas.create_text(
                522.0,
                258.0,
                anchor="nw",
                text="Wind snelheid:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            canvas.create_text(
                385.0,
                262.0,
                anchor="nw",
                text="Temp:",
                fill="#000000",
                font=("Inter", 15 * -1),
            )

            button_1 = Button(
                Frame,
                text="Zoeken",
                borderwidth=0,
                highlightthickness=0,
                command=self.fetchWeather,
                relief="flat",
            )
            button_1.place(x=38.0, y=186.0, width=65.0, height=21.0)

        except Exception as e:
            print(f"An error occurred [run]: {e}")
