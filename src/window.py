import tkinter as tk


class Window:
    """
    Class Window creates main window with tk.Tk(),
    set and save basic variables connected with window

    Description of variables:
    width_screen: screen width in pixels
    height_screen: screen height in pixels
    size_of_text: size of text in pixels
    width_screen_ratio: coefficient to make screen width independent of monitor resolution
    height_screen_ratio: coefficient to make screen width independent of monitor resolution
    """
    wind: tk.Tk
    width_screen: int
    height_screen: int
    size_of_text: int
    width_screen_ratio = 1.3
    height_screen_ratio = 1.3
    size_of_text_ratio = 50

    def __init__(self):
        self.wind = tk.Tk()
        self.width_screen = int(self.wind.winfo_screenwidth() / self.width_screen_ratio)
        self.height_screen = int(self.wind.winfo_screenheight() / self.height_screen_ratio)
        self.size_of_text = int(self.width_screen / self.size_of_text_ratio)

        self.wind.title('Clicker')
        self.wind.geometry(str(self.width_screen) + "x" + str(self.height_screen))
        self.wind.resizable(width=False, height=False)
