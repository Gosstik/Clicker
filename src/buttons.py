import tkinter as tk


class Buttons:
    """
    class Buttons creates buttons for interactions with user
    and display them on main window

    functions for making buttons:
    def create_button_autoclicker(self, window, labels):
    def create_button_boost_click(self, window, labels):
    def create_button_boost_cpc(self, window, labels):
    def create_button_double_speed(self, window, labels):
    """
    # common variables for buttons
    button_font_ratio = 0.8
    button_x_ratio = 0.6
    button_width_ratio = 0.3
    button_height_ratio = 0.2

    # special variables for buttons
    button_autoclicker_y_ratio = 0.01
    button_boost_click_y_ratio = 0.22
    button_boost_cpc_y_ratio = 0.43
    button_double_speed_y_ratio = 0.64

    def __init__(self, window, labels):
        window.wind.bind('<space>', lambda event: labels.update(event, window, False))
        self.create_button_autoclicker(window, labels)
        self.create_button_boost_click(window, labels)
        self.create_button_boost_cpc(window, labels)
        self.create_button_double_speed(window, labels)

    def create_button_autoclicker(self, window, labels):
        self.button_autoclicker = tk.Button(window.wind,
                                            text=("Boost auto clicker"
                                                  "\nLevel: " + str(labels.autoclicker_level) +
                                                  "\nCost: $ " + labels.get_val(labels.auto_clicker_cost) +
                                                  "\nUpdate: +1"),
                                            font=("Comic Sans MS", int(window.size_of_text *
                                                                       self.button_font_ratio), "bold"),
                                            bg="green",
                                            fg="blue",
                                            command=lambda: labels.autoclicker(window, self.button_autoclicker))
        self.button_autoclicker.place(x=window.width_screen * self.button_x_ratio,
                                      y=window.height_screen * self.button_autoclicker_y_ratio,
                                      width=window.width_screen * self.button_width_ratio,
                                      height=window.height_screen * self.button_height_ratio)

    def create_button_boost_click(self, window, labels):
        self.button_boost_click = tk.Button(window.wind,
                                            text=("Boost score per click"
                                                  "\nLevel: " + str(labels.boost_click_level) +
                                                  "\nCost: $ " + labels.get_val(labels.button_boost_click_cost) +
                                                  "\nUpdate: +1"),
                                            font=("Comic Sans MS", int(window.size_of_text *
                                                                       self.button_font_ratio), "bold"),
                                            bg="green",
                                            fg="blue",
                                            command=lambda: labels.boost_click(window, self.button_boost_click))
        self.button_boost_click.place(x=window.width_screen * self.button_x_ratio,
                                      y=window.height_screen * self.button_boost_click_y_ratio,
                                      width=window.width_screen * self.button_width_ratio,
                                      height=window.height_screen * self.button_height_ratio)

    # (cpc = coins per click)
    def create_button_boost_cpc(self, window, labels):
        self.button_boost_cpc = tk.Button(window.wind,
                                          text=("Number of coins per click"
                                                "\nLevel: " + str(labels.boost_cpc_level) +
                                                "\nCost: $ " + labels.get_val(labels.button_cpc_cost) +
                                                "\nUpdate: +" + labels.correct_str(str(labels.update_cpc))),
                                          font=("Comic Sans MS", int(window.size_of_text *
                                                                     self.button_font_ratio), "bold"),
                                          bg="green",
                                          fg="blue",
                                          command=lambda: labels.boost_cpc(window, self.button_boost_cpc))
        self.button_boost_cpc.place(x=window.width_screen * self.button_x_ratio,
                                    y=window.height_screen * self.button_boost_cpc_y_ratio,
                                    width=window.width_screen * self.button_width_ratio,
                                    height=window.height_screen * self.button_height_ratio)

    def create_button_double_speed(self, window, labels):
        self.button_double_speed = tk.Button(window.wind,
                                             text=("Double speed of autoclicker"
                                                   "\n for 5 seconds "
                                                   "\nNumber of uses: " + str(labels.double_speed_num_of_uses) +
                                                   "\nCost: $ " +
                                                   labels.get_val(labels.double_speed_cost)),
                                             font=("Comic Sans MS", int(window.size_of_text *
                                                                        self.button_font_ratio), "bold"),
                                             bg="green",
                                             fg="blue",
                                             command=lambda: labels.double_speed(window, self.button_double_speed))
        self.button_double_speed.place(x=window.width_screen * self.button_x_ratio,
                                       y=window.height_screen * self.button_double_speed_y_ratio,
                                       width=window.width_screen * self.button_width_ratio,
                                       height=window.height_screen * self.button_height_ratio)
