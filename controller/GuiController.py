from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
from helpers.Helpers import Helpers
from config import config
from controller.WeatherGuiController import WeatherGuiController


class GuiController:
    # initilianze
    def __init__(self):
        self.root = None
        self.main_frame = None
        self.main_canvas = None
        self.weather_frame = None
        self.chatbot_frame = None
        self.news_frame = None
        self.filmroulete_frame = None

        # images
        self.button_image_1 = None
        self.button_image_2 = None
        self.button_image_3 = None
        self.button_image_4 = None

    def _getHelpersService(self) -> Helpers:
        return Helpers()

    def relative_to_assets(self, file: str) -> Path:
        current_dir_path: str = (
            self._getHelpersService().getCurrentWorkingDirFolderPath()
        )
        assets_path: str = f"{current_dir_path}/builds/build_main/assets/frame0"
        return assets_path / Path(file)

    def getRootWindow(self):
        try:
            return self.root
        except Exception as e:
            print(f"An error occurred [getRootWindow]: {e}")

    def getMainFrame(self):
        try:
            return self.main_frame
        except Exception as e:
            print(f"An error occurred [getMainFrame]: {e}")

    def getMainCanvas(self):
        try:
            return self.main_canvas
        except Exception as e:
            print(f"An error occurred [getMainCanvas]: {e}")

    def getWeatherFrame(self):
        try:
            return self.weather_frame
        except Exception as e:
            print(f"An error occurred [getWeatherFrame]: {e}")

    def getFilmRouleteFrame(self):
        try:
            return self.filmroulete_frame
        except Exception as e:
            print(f"An error occurred [getFilmRouleteFrame]: {e}")

    def openWeatherFrame(self):
        try:
            main_frame: Frame = self.getMainFrame()
            main_frame.pack_forget()

            weather_frame: Frame = self.getWeatherFrame()
            weather_frame.pack(fill="both", expand=True)
        except Exception as e:
            print(f"An error occurred [openWeatherFrame]: {e}")

    def openFilmRouleteFrame(self):
        try:
            main_frame: Frame = self.getMainFrame()
            main_frame.pack_forget()

            film_roulete_frame: Frame = self.getFilmRouleteFrame()
            film_roulete_frame.pack(fill="both", expand=True)
        except Exception as e:
            print(f"An error occurred [openFilmRouleteFrame]: {e}")


    def createMainFrame(self):
        try:
            frame = Frame(self.getRootWindow(), bg="white", height=700, width=700)
            frame.pack()
            self.main_frame = frame
            return True
        except Exception as e:
            print(f"An error occurred [getRootWindow]: {e}")

    def openMainFrame(self) -> bool:
        try:
            # close weather frame
            self.getWeatherFrame().pack_forget()

            self.getMainFrame().pack(fill="both", expand=True)
            return True
        except Exception as e:
            print(f"An error occurred [openMainFrame]: {e}")

    def createWeatherFrame(self):
        try:
            weather_frame = self.weather_frame = Frame(
                self.getRootWindow(), bg="white", height=700, width=700
            )

            controller: WeatherGuiController = WeatherGuiController()
            controller.run(weather_frame)

            button_to_frame1 = Button(
                self.getWeatherFrame(), text="Terug", command=self.openMainFrame
            )
            button_to_frame1.pack(pady=75)

        except Exception as e:
            print(f"An error occurred [createWeatherFrame]: {e}")

  
    def createFilmRouleteFrame(self) ->bool:
        try:
            # create frame for film roullete
            filmroulete_frame = self.filmroulete_frame = Frame(
                self.getRootWindow(), bg="white", height=700, width=700
            )
            label = Label(
                filmroulete_frame, text="This is Frame for roullete", bg="lightgreen"
            )
            label.pack(pady=20)
            return True
        except Exception as e:
            print(f"An error occurred [createFilmRouleteFrame]: {e}")

    def intitFrames(self) -> bool:
        try:
            # create frame for weather
            self.createMainFrame()
            self.createWeatherFrame()
            # self.createChatBotFrame()
            # self.createNewsFrame()
            self.createFilmRouleteFrame()
            return True
        except Exception as e:
            print(f"An error occurred [intitFrames]: {e}")

    def intiRootWindow(self) -> bool:
        try:
            root = Tk()
            root.title(config.APP_NAME)
            root.geometry("700x400")
            self.root = root
            return True
        except Exception as e:
            print(f"An error occurred [intiRootWindow]: {e}")

    def createMainCanvas(self) -> bool:
        try:
            # Create a canvas inside frame1
            canvas = Canvas(self.getMainFrame(), bg="white", height=700, width=700)
            canvas.pack()
            self.main_canvas = canvas
            return True
        except Exception as e:
            print(f"An error occurred [createMainCanvas]: {e}")

    def createSideBar(self) -> bool:
        try:
            canvas: Canvas = self.getMainCanvas()
            # Tuple of dimensions of the rectangle (left, top, right, bottom)
            pos = (0, 0, 175, 600)
            canvas.create_rectangle(pos, fill="#0E1E3D", outline="")

            # Create header text on the canvas
            canvas.create_text(
                329.0,
                0.0,
                anchor="nw",
                text="PocketApps",
                fill="#000000",
                font=("HachiMaruPop Regular", 32 * -1),
            )

            return True
        except Exception as e:
            print(f"An error occurred [createSideBar]: {e}")

    def createHr(self) -> bool:
        try:
            canvas: Canvas = self.getMainCanvas()
            # Create hr line
            canvas.create_rectangle(0.0, 53.0, 725.0, 55.0, fill="#D9D9D9", outline="")
            return True
        except Exception as e:
            print(f"An error occurred [createHr]: {e}")

    def createWeatherButton(self) -> bool:
        try:
            frame: Frame = self.getMainFrame()

            # https://stackoverflow.com/questions/22200003/tkinter-button-not-showing-image
            self.button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_1.png")
            )
            # assign the image to a global, otherwuse the garbage collceter will render the image wite

            button_1 = Button(
                frame,
                image=self.button_image_1,
                text="Hello",
                borderwidth=0,
                highlightthickness=0,
                command=self.openWeatherFrame,
                relief="flat",
            )
            button_1.place(x=5.0, y=85.0, width=115.0, height=23.0)
            return True

        except Exception as e:
            print(f"An error occurred [createWeatherButton]: {e}")

    def createFilmRouleteButton(self) -> bool:
        try:
            frame: Frame = self.getMainFrame()

            self.button_image_4 = PhotoImage(
                file=self.relative_to_assets("button_4.png")
            )
            button_4 = Button(
                frame,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=self.openFilmRouleteFrame,
                relief="flat",
            )
            button_4.place(x=5.0, y=119.0, width=115.0, height=23.0)
            return True
            #button_4.place(x=5.0, y=157.0, width=115.0, height=24.0)
        except Exception as e:
            print(f"An error occurred [createFilmRouleteButton]: {e}")

    def initUI(self) -> None:
        try:
            self.intiRootWindow()
            self.intitFrames()
            self.createMainCanvas()
            self.createSideBar()
            self.createHr()

            # add buttons
            self.createWeatherButton()
            self.createFilmRouleteButton()

            # Prevent window from being resized
            self.getRootWindow().resizable(False, False)

            # Run the main loop
            self.getRootWindow().mainloop()

        except Exception as e:
            print(f"An error occurred [initUI]: {e}")

    def run(self) -> None:
        try:
            self.initUI()
        except Exception as e:
            print(f"An error occurred [GuiController-run]: {e}")
