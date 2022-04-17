import tkinter as tk


class Buttons:
    def __init__(self, window, labels):
        window.wind.bind('<space>', lambda sel: labels.update())

        # button_autoclicker
        tmp_text = "Boost auto clicker\ncost: $ " + labels.get_val(labels.auto_clicker_cost) + "\nUpdate: +1"
        self.button_autoclicker = tk.Button(window.wind,
                                            text=tmp_text,
                                            font=("Comic Sans MS", int(window.size_of_text * 0.8), "bold"),
                                            bg="green",
                                            fg="blue",
                                            command=lambda: labels.boost_autoclicker(window, self.button_autoclicker))
        self.button_autoclicker.place(x=window.width_screen * 0.6,
                                      y=window.height_screen * 0.01,
                                      width=window.width_screen * 0.3,
                                      height=window.height_screen * 0.2)

        # button_boost_click
        tmp_text = "Boost score per click\ncost: $ " + labels.get_val(labels.score_per_click) + "\nUpdate: +1"
        self.button_boost_click = tk.Button(window.wind,
                                            text=tmp_text,
                                            font=("Comic Sans MS", int(window.size_of_text * 0.8), "bold"),
                                            bg="green",
                                            fg="blue",
                                            command=lambda: labels.boost_click(window, self.button_boost_click))
        self.button_boost_click.place(x=window.width_screen * 0.6,
                                      y=window.height_screen * 0.22,
                                      width=window.width_screen * 0.3,
                                      height=window.height_screen * 0.2)

        # labels.update_autoclicker(window)
