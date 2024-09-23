from helpers.Helpers import Helpers
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from pathlib import Path
from model.FilmRouleteModel import FilmRouleteModel


class FilmRouleteController:
    # initilianze
    def __init__(self):
        self.frame = None
        self.canvas = None
        
        #text fields
        self.canvas_title_item = None
        self.canvas_rating_item = None
        self.canvas_description_item = None

    def _getHelpersService(self) -> Helpers:
        return Helpers()
    
    def _getFilmRouleteModel(self) ->FilmRouleteModel:
        return FilmRouleteModel()

    def setFrame(self, frame: Frame):
        try:
            self.frame = frame
        except Exception as e:
            print(f"An error occurred [setFrame]: {e}")

    def setCanvas(self, canvas: Canvas):
        try:
            self.canvas = canvas
        except Exception as e:
            print(f"An error occurred [setCanvas]: {e}")

    def getFrame(self) -> Frame:
        try:
            return self.frame
        except Exception as e:
            print(f"An error occurred [getFrame]: {e}")

    def getCanvas(self) -> Canvas:
        try:
            return self.canvas
        except Exception as e:
            print(f"An error occurred [getCanvas]: {e}")

    def relative_to_assets(self, file: str):
        try:
            current_dir_path: str = (
                self._getHelpersService().getCurrentWorkingDirFolderPath()
            )
            assets_path: str = (
                f"{current_dir_path}/builds/build_film/build/assets/frame0"
            )
            return assets_path / Path(file)
        except Exception as e:
            print(f"An error occurred [relative_to_assets]: {e}")

    def getRandomFilm(self) -> None:
        try:
            canvas: Canvas = self.getCanvas()
            results: dict = self._getFilmRouleteModel().fetchFilm()

            canvas.itemconfig(self.canvas_description_item, text=results["description"])
            canvas.itemconfig(self.canvas_rating_item, text=results["rating"])
            canvas.itemconfig(self.canvas_title_item, text=results["title"])

        except Exception as e:
            print(f"An error occurred [getRandomFilm]: {e}")

    def createSearchButton(self) -> bool:
        try:
            canvas: Canvas = self.getCanvas()
            button_1 = Button(
                canvas,
                text="Zoeken",
                borderwidth=0,
                highlightthickness=0,
                command= self.getRandomFilm,
                relief="flat",
            )
            button_1.place(x=228.0, y=280.0, width=188.0, height=39.0)
        except Exception as e:
            print(f"An error occurred [createSearchButton]: {e}")

    def createFrame(self) -> bool:
        try:
            frame: Frame = self.getFrame()

            canvas = Canvas(
                frame,
                bg="#FFFFFF",
                height=343,
                width=672,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )
            canvas.place(x=0, y=0)
            self.setCanvas(canvas)
        except Exception as e:
            print(f"An error occurred [createFrame]: {e}")

    def initUI(self):
        try:
            self.createFrame()
            self.createSearchButton()
            self.createTitle()
            self.createRating()
            self.createDescription()

            self._getHelpersService().printGameOptionsToUser(
                header=True, clear_console=True
            )

        except Exception as e:
            print(f"An error occurred [initUI]: {e}")

    def createTitle(self) -> bool:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_title_item = canvas.create_text(
                293.0,
                24.0,
                anchor="nw",
                text="Titel...",
                fill="#000000",
                font=("Inter", 20 * -1),
            )
            self.canvas_title_item = canvas_title_item
            return True
        except Exception as e:
            print(f"An error occurred [createTitle]: {e}")

    def createRating(self) -> bool:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_rating_item = canvas.create_text(
                298.0,
                253.0,
                anchor="nw",
                text="Rating",
                fill="#000000",
                font=("Inter", 16 * -1),
            )
            self.canvas_rating_item = canvas_rating_item
            return True
        except Exception as e:
            print(f"An error occurred [createRating]: {e}")

    def createDescription(self) -> bool:
        try:
            canvas: Canvas = self.getCanvas()
            canvas_description_item = canvas.create_text(
                0,
                134.0,
                anchor="nw",
                text="Omschrijving",
                fill="#000000",
                font=("Inter", 16 * -1),
            )
            self.canvas_description_item  = canvas_description_item
            return True
        except Exception as e:
            print(f"An error occurred [createDescription]: {e}")

    def run(self, frame: Frame) -> None:
        try:
            self.setFrame(frame)
            self.initUI()
            self._getHelpersService().printGameOptionsToUser(
                header=True, clear_console=True
            )
        except Exception as e:

            print(f"An error occurred [run]: {e}")
