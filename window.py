import tkinter as tk


class Window:
    wind: tk.Tk
    width_screen: int
    height_screen: int
    size_of_text: int  # must depend on the resolution of the monitor

    def __init__(self):
        self.wind = tk.Tk()
        self.width_screen = int(self.wind.winfo_screenwidth() / 1.3)
        self.height_screen = int(self.wind.winfo_screenheight() / 1.3)
        self.size_of_text = int(self.width_screen / 50)

        self.wind.title('Clicker')
        self.wind.geometry(str(self.width_screen) + "x" + str(self.height_screen))
        self.wind.resizable(width=False, height=False)
        self.wind['bg'] = "black"
