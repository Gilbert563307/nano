from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from helpers.Helpers import Helpers
from config import config

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ssemp\Documents\MYHU\PROG\nano\build\assets\frame0")

class GuiController:
    # initilianze
    def __init__(self):
        pass

    def _getHelpersService(self) -> Helpers:
        return Helpers()
    
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def test_run(self):
        try:
            pass
            # #main windows
            # root: tk = tk.Tk()

            # #set tilte name
            # root.title(config.APP_NAME)

            # #label
            # label = tk.Label(root, text="Hello world")
            # label.grid()

            # #pass in root bebause this is our parent windows
            # btn = tk.Button(root, text="Button 1", command=self.getData)
            # #add to our window
            # btn.grid()

            
            # #keep window open start main loop
            # root.mainloop()

            # self._getHelpersService().printGameOptionsToUser(header=True, clear_console=True)
        except Exception as e:
            # Handles the exception
            print(f"An error occurred [GuiController-run]: {e}")

    #ui generated via tutorial https://www.youtube.com/watch?v=oLxFqpUbaAE: github: https://github.com/ParthJadhav/Tkinter-Designer
    def run(self):
        try:
            window = Tk()

            window.geometry("736x261")
            window.configure(bg = "#FFFFFF")


            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 261,
                width = 736,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            canvas.create_rectangle(
                0.0,
                0.0,
                124.0,
                261.0,
                fill="#0E1E3D",
                outline="")

            canvas.create_text(
                329.0,
                0.0,
                anchor="nw",
                text="PocketApps",
                fill="#000000",
                font=("HachiMaruPop Regular", 32 * -1)
            )

            canvas.create_rectangle(
                0.0,
                53.0,
                725.0,
                55.0,
                fill="#D9D9D9",
                outline="")

            button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_1.png"))
            button_1 = Button(
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_1 clicked"),
                relief="flat"
            )
            button_1.place(
                x=20.0,
                y=85.0,
                width=84.0,
                height=23.0
            )

            button_image_2 = PhotoImage(
                file=self.relative_to_assets("button_2.png"))
            button_2 = Button(
                image=button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_2 clicked"),
                relief="flat"
            )
            button_2.place(
                x=20.0,
                y=119.0,
                width=84.0,
                height=23.0
            )

            button_image_3 = PhotoImage(
                file=self.relative_to_assets("button_3.png"))
            button_3 = Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_3 clicked"),
                relief="flat"
            )
            button_3.place(
                x=18.0,
                y=194.0,
                width=86.0,
                height=23.0
            )

            canvas.create_text(
                18.0,
                20.0,
                anchor="nw",
                text="Menu",
                fill="#FFFFFF",
                font=("Poppins Regular", 15 * -1)
            )

            button_image_4 = PhotoImage(
                file=self.relative_to_assets("button_4.png"))
            button_4 = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_4 clicked"),
                relief="flat"
            )
            button_4.place(
                x=20.0,
                y=158.0,
                width=84.0,
                height=23.0
            )
            window.resizable(False, False)
            window.mainloop()

            self._getHelpersService().printGameOptionsToUser(header=True, clear_console=True)
        except Exception as e:
            print(f"An error occured [GuiController-run] {e}")