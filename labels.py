import tkinter as tk
import time


class MyLabels:
    # main variables
    score = 0
    score_per_click = 1
    coins = 0
    coins_per_click = 0.05
    update_cpc = 0.05
    level = 1
    score_lvl_up = 100
    highest_score = 0
    # for autoclicker
    auto_clicks_per_sec = 0
    first_call_autoclicker = True
    is_double_speed = False
    time_start_double_speed = 0
    time_end_double_speed = 0
    # costs
    auto_clicker_cost = 1
    button_boost_click_cost = 1
    button_cpc_cost = 2
    double_speed_cost = 10
    # levels of bonuses
    autoclicker_level = 1
    boost_click_level = 1
    boost_cpc_level = 1  # (cpc = coins per click)
    double_speed_num_of_uses = 0

    def __init__(self, window):
        self.label_score_x = 0
        self.label_score_y = 0
        self.label_coins_x = 0
        self.label_coins_y = window.size_of_text * 2
        self.label_level_x = 0
        self.label_level_y = window.size_of_text * 4
        self.label_score_lvl_up_x = 0
        self.label_score_lvl_up_y = window.size_of_text * 6
        self.label_auto_clicks_per_sec_x = 0
        self.label_auto_clicks_per_sec_y = window.size_of_text * 8
        self.label_score_per_click_x = 0
        self.label_score_per_click_y = window.size_of_text * 10
        self.label_coins_per_click_x = 0
        self.label_coins_per_click_y = window.size_of_text * 12

        self.label_highest_score_x = window.size_of_text
        self.label_highest_score_y = window.height_screen * 0.87

        self.update_labels(window)

    def update_labels(self, window):
        self.update_label_score(window)
        self.update_label_coins(window)
        self.update_label_level(window)
        self.update_label_score_lvl_up(window)
        self.update_label_auto_clicks_per_sec(window)
        self.update_label_score_per_click(window)
        self.update_label_coins_per_click(window)
        self.update_label_highest_score(window)

    def update_label_score(self, window):
        self.label_score = tk.Label(window.wind,
                                    text="Score: " + str(self.score),
                                    font=("Comic Sans MS", window.size_of_text, "bold"),
                                    bg="black",
                                    fg="white")
        self.label_score.place(x=self.label_score_x, y=self.label_score_y)

    def update_label_coins(self, window):
        self.label_coins = tk.Label(window.wind,
                                    text="Coins: $ " + self.get_val(self.coins),
                                    font=("Comic Sans MS", window.size_of_text, "bold"),
                                    bg="black",
                                    fg="white")
        self.label_coins.place(x=self.label_coins_x, y=self.label_coins_y)

    def update_label_level(self, window):
        self.label_level = tk.Label(window.wind,
                                    text="Level: " + str(self.level),
                                    font=("Comic Sans MS", window.size_of_text, "bold"),
                                    bg="black",
                                    fg="white")
        self.label_level.place(x=self.label_level_x, y=self.label_level_y)

    def update_label_score_lvl_up(self, window):
        self.label_score_lvl_up = tk.Label(window.wind,
                                           text="Score to level up: " + str(self.score_lvl_up),
                                           font=("Comic Sans MS", window.size_of_text, "bold"),
                                           bg="black",
                                           fg="white")
        self.label_score_lvl_up.place(x=self.label_score_lvl_up_x, y=self.label_score_lvl_up_y)

    def update_label_auto_clicks_per_sec(self, window):
        self.label_auto_clicks_per_sec = tk.Label(window.wind,
                                                  text="Number of auto-clicks per second: " + str(
                                                      self.auto_clicks_per_sec),
                                                  font=("Comic Sans MS", window.size_of_text, "bold"),
                                                  bg="black",
                                                  fg="white")
        self.label_auto_clicks_per_sec.place(x=self.label_auto_clicks_per_sec_x, y=self.label_auto_clicks_per_sec_y)

    def update_label_score_per_click(self, window):
        self.label_score_per_click = tk.Label(window.wind,
                                              text="Number of points per click: " + str(self.score_per_click),
                                              font=("Comic Sans MS", window.size_of_text, "bold"),
                                              bg="black",
                                              fg="white")
        self.label_score_per_click.place(x=self.label_score_per_click_x, y=self.label_score_per_click_y)

    def update_label_coins_per_click(self, window):
        self.label_coins_per_click = tk.Label(window.wind,
                                              text="Number of coins per click: " + self.get_val(self.coins_per_click),
                                              font=("Comic Sans MS", window.size_of_text, "bold"),
                                              bg="black",
                                              fg="white")
        self.label_coins_per_click.place(x=self.label_coins_per_click_x, y=self.label_coins_per_click_y)

    # reading from file
    def update_label_highest_score(self, window):
        file = open('highest score', 'r')
        self.highest_score = int(file.read())
        file.close()
        self.label_highest_score = tk.Label(window.wind,
                                            text="Highest score: " + str(self.highest_score),
                                            font=("Comic Sans MS", int(window.size_of_text * 2.5), "bold"),
                                            bg="black",
                                            fg="white")
        self.label_highest_score.place(x=self.label_highest_score_x, y=self.label_highest_score_y)

    def update(self, event, window, autoclicker_calls):
        self.update_score(autoclicker_calls)
        self.update_highest_score()
        self.update_coins(autoclicker_calls)
        self.update_score_lvl_up()
        self.update_image()

    def update_score(self, autoclicker_calls):
        if not autoclicker_calls:
            self.score += self.score_per_click
        else:
            self.score += self.score_per_click * self.auto_clicks_per_sec

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

    def update_coins(self, autoclicker_calls):
        if not autoclicker_calls:
            self.coins += self.coins_per_click
        else:
            self.coins += self.coins_per_click * self.auto_clicks_per_sec

    def update_score_lvl_up(self):
        if self.score >= self.score_lvl_up:
            self.score_lvl_up += self.score_lvl_up * self.level
            self.update_level()

    def update_level(self):
        self.level += 1

    def update_autoclicker(self, window):
        if not self.is_double_speed:
            self.update(0, window, True)
            window.wind.after(1000, lambda: self.update_autoclicker(window))
        else:
            self.time_end_double_speed = time.time()
            if self.time_end_double_speed - self.time_start_double_speed < 5:
                self.update(0, window, True)
                window.wind.after(500, lambda: self.update_autoclicker(window))
            else:
                self.is_double_speed = False
                self.time_end_double_speed = self.time_start_double_speed = 0
                self.update(0, window, True)
                window.wind.after(1000, lambda: self.update_autoclicker(window))

    # for button_autoclicker
    def autoclicker(self, window, button_autoclicker):
        if self.coins < self.auto_clicker_cost:
            return
        else:
            self.autoclicker_level += 1
            self.coins -= self.auto_clicker_cost
            self.auto_clicker_cost += 0.5 * self.autoclicker_level
            button_autoclicker['text'] = ("Boost auto clicker"
                                          "\nLevel: " + str(self.autoclicker_level) +
                                          "\nCost: $ " + self.get_val(self.auto_clicker_cost) +
                                          "\nUpdate: +1")
            self.auto_clicks_per_sec += 1
            if self.first_call_autoclicker:
                self.update_autoclicker(window)  # CALLS AFTER!!!
                self.first_call_autoclicker = False
            self.update_image()

    # for button_boost_click
    def boost_click(self, window, button_boost_click):
        if self.coins < self.button_boost_click_cost:
            return
        else:
            self.boost_click_level += 1
            self.coins -= self.button_boost_click_cost
            self.button_boost_click_cost += 0.5 * self.boost_click_level
            button_boost_click['text'] = ("Boost score per click"
                                          "\nLevel: " + str(self.boost_click_level) +
                                          "\nCost: $ " + self.get_val(self.button_boost_click_cost) +
                                          "\nUpdate: +1")
            self.score_per_click += 1
            self.update_image()

    # for button_boost_cpc
    # (cpc = coins per click)
    def boost_cpc(self, window, button_boost_cpc):
        if self.coins < self.button_cpc_cost:
            return
        else:
            self.boost_cpc_level += 1
            self.coins -= self.button_cpc_cost
            self.button_cpc_cost += 1.5 * self.boost_cpc_level
            button_boost_cpc['text'] = ("Number of coins per click"
                                        "\nLevel: " + str(self.boost_cpc_level) +
                                        "\nCost: $ " + self.get_val(self.button_cpc_cost) +
                                        "\nUpdate: +" + self.correct_str(str(self.update_cpc)))
            self.coins_per_click += self.update_cpc
            self.update_image()

    # for button_double_speed
    def double_speed(self, window, button_double_speed):
        if not self.first_call_autoclicker and self.coins >= self.double_speed_cost:
            self.double_speed_num_of_uses += 1
            self.coins -= self.double_speed_cost
            self.double_speed_cost += 10 * self.double_speed_num_of_uses
            button_double_speed['text'] = ("Double speed of autoclicker"
                                           "\n for 5 seconds "
                                           "\nNumber of uses: " + str(self.double_speed_num_of_uses) +
                                           "\nCost: $ " + self.get_val(self.double_speed_cost))
            self.time_end_double_speed = 0
            self.time_start_double_speed = time.time()
            self.is_double_speed = True
            window.wind.after_cancel(lambda: self.update_autoclicker(window))
            self.update_image()

    def update_image(self):
        self.label_score['text'] = "Score: " + str(self.score)
        self.label_score.place(x=self.label_score_x, y=self.label_score_y)

        self.label_coins['text'] = "Coins: $ " + self.correct_str(str(round(self.coins, 2)))
        self.label_coins.place(x=self.label_coins_x, y=self.label_coins_y)

        self.label_level['text'] = "Level: " + str(self.level)
        self.label_level.place(x=self.label_level_x, y=self.label_level_y)

        self.label_score_lvl_up['text'] = "Score to level up: " + str(self.score_lvl_up)
        self.label_score_lvl_up.place(x=self.label_score_lvl_up_x, y=self.label_score_lvl_up_y)

        self.label_auto_clicks_per_sec['text'] = "Number of auto-clicks per second: " + str(self.auto_clicks_per_sec)
        self.label_auto_clicks_per_sec.place(x=self.label_auto_clicks_per_sec_x, y=self.label_auto_clicks_per_sec_y)

        self.label_score_per_click['text'] = "Number of points per click: " + str(self.score_per_click)
        self.label_score_per_click.place(x=self.label_score_per_click_x, y=self.label_score_per_click_y)

        self.label_coins_per_click['text'] = "Number of coins per click: " + self.get_val(self.coins_per_click)
        self.label_coins_per_click.place(x=self.label_coins_per_click_x, y=self.label_coins_per_click_y)

        self.label_highest_score['text'] = "Highest score: " + str(self.highest_score)
        self.label_highest_score.place(x=self.label_highest_score_x, y=self.label_highest_score_y)

    def correct_str(self, string):  # returns a number with 2 digits after the dot
        leng = len(string)
        if '.' not in string:
            return string + '.00'
        elif string[leng - 2] == '.':
            return string + '0'
        elif string[leng - 3] == '.':
            return string

    def get_val(self, val):
        return self.correct_str(str(round(val, 2)))
