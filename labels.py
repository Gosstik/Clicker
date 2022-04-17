import tkinter as tk


class MyLabels:
    score = 0
    score_per_click = 1
    coins_per_click = 0.5
    coins = 0
    level = 1
    clicks_left = 10  # the remaining number of clicks to the next level
    auto_clicks_per_sec = 0
    auto_clicker_cost = 1
    button_boost_click_cost = 1
    first_call_boost_autoclicker = True

    def __init__(self, window):
        self.label_score_x = 0
        self.label_score_y = 0
        self.label_coins_x = 0
        self.label_coins_y = window.size_of_text * 2
        self.label_level_x = 0
        self.label_level_y = window.size_of_text * 4
        self.label_clicks_left_x = 0
        self.label_clicks_left_y = window.size_of_text * 6
        self.label_auto_clicks_per_sec_x = 0
        self.label_auto_clicks_per_sec_y = window.size_of_text * 8
        self.label_score_per_click_x = 0
        self.label_score_per_click_y = window.size_of_text * 10
        self.coins_per_click_x = 0
        self.coins_per_click_y = window.size_of_text * 12

        self.update_label(window)

    def update_label(self, window):
        self.label_score = self.init_label(window,
                                           "Score: " + str(self.score),
                                           "black",
                                           "white",
                                           self.label_score_x,
                                           self.label_score_y)
        self.label_coins = self.init_label(window,
                                           "Coins: $ " + self.get_val(self.coins),
                                           "black",
                                           "white",
                                           self.label_coins_x,
                                           self.label_coins_y)
        self.label_level = self.init_label(window,
                                           "Level: " + str(self.level),
                                           "black",
                                           "white",
                                           self.label_level_x,
                                           self.label_level_y)
        self.label_clicks_left = self.init_label(window,
                                                 "Need Clicks to next level: " + str(self.clicks_left),
                                                 "black",
                                                 "white",
                                                 self.label_clicks_left_x,
                                                 self.label_clicks_left_y)
        self.label_auto_clicks_per_sec = self.init_label(window,
                                                         "Number of auto-clicks per second: " + str(self.auto_clicks_per_sec),
                                                         "black",
                                                         "white",
                                                         self.label_auto_clicks_per_sec_x,
                                                         self.label_auto_clicks_per_sec_y)
        self.label_score_per_click = self.init_label(window,
                                                     "Number of points per click: " + str(self.score_per_click),
                                                     "black",
                                                     "white",
                                                      self.label_score_per_click_x,
                                                      self.label_score_per_click_y)
        self.label_coins_per_click = self.init_label(window,
                                                     "Number of coins per click: " + self.get_val(self.coins_per_click),
                                                     "black",
                                                     "white",
                                                     self.coins_per_click_x,
                                                     self.coins_per_click_y)

    def init_label(self, window, lab_text, lab_bg, lab_fg, place_x, place_y):
        tmp = tk.Label(window.wind,
                       text=lab_text,
                       font=("Comic Sans MS", window.size_of_text, "bold"),
                       bg=lab_bg,
                       fg=lab_fg)
        tmp.place(x=place_x, y=place_y)
        return tmp

    def update(self):
        self.update_score()
        self.update_coins()
        self.update_clicks_left()
        self.update_image()

    def update_score(self):
        self.score += self.score_per_click

    def update_coins(self):
        self.coins += self.coins_per_click

    def update_clicks_left(self):
        self.clicks_left -= 1
        if self.clicks_left <= 0:
            self.update_level()
            self.clicks_left = self.level * 10

    def update_level(self):
        self.level += 1

    def boost_autoclicker(self, window, button_autoclicker):
        if self.coins < self.auto_clicker_cost:
            return
        else:
            self.coins -= self.auto_clicker_cost
            self.auto_clicker_cost += 0.5
            button_autoclicker['text'] = "Boost auto clicker\ncost: $ " + self.get_val(self.auto_clicker_cost) + "\nUpdate: +1"
            self.auto_clicks_per_sec += 1
            if self.first_call_boost_autoclicker:
                window.wind.after(1000, lambda: self.update_autoclicker(window))
                self.first_call_boost_autoclicker = False
            self.update_image()
            self.label_auto_clicks_per_sec = self.init_label(window,
                                                             "Number of auto-clicks per second: " + str(
                                                                 self.auto_clicks_per_sec),
                                                             "black",
                                                             "white",
                                                             self.label_auto_clicks_per_sec_x,
                                                             self.label_auto_clicks_per_sec_y)
            # self.update_label(window)

    def update_autoclicker(self, window):
        self.update()
        window.wind.after(1000, lambda: self.update_autoclicker(window))

    def boost_click(self, window, button_boost_click):
        if self.coins < self.button_boost_click_cost:
            return
        else:
            self.coins -= self.button_boost_click_cost
            self.button_boost_click_cost += 0.5
            tmp_text = "Boost score per click\ncost: $ " + self.get_val(self.button_boost_click_cost) + "\nUpdate: +1"
            button_boost_click['text'] = tmp_text
            self.score_per_click += 1
            self.update_image()
            self.label_score_per_click = self.init_label(window,
                                                         "Number of points per click: " + str(self.score_per_click),
                                                         "black",
                                                         "white",
                                                         self.label_score_per_click_x,
                                                         self.label_score_per_click_y)
            # self.update_label(window)

    def update_image(self):
        self.label_score['text'] = "Score: " + str(self.score)
        self.label_score.place(x=self.label_score_x, y=self.label_score_y)

        self.label_coins['text'] = "Coins: $ " + self.correct_str(str(round(self.coins, 2)))
        self.label_coins.place(x=self.label_coins_x, y=self.label_coins_y)

        self.label_clicks_left['text'] = "Need Clicks to next level: " + str(self.clicks_left)
        self.label_clicks_left.place(x=self.label_clicks_left_x, y=self.label_clicks_left_y)

        self.label_level['text'] = "Level: " + str(self.level)
        self.label_level.place(x=self.label_level_x, y=self.label_level_y)

    def correct_str(self, string_coins):
        leng = len(string_coins)
        if '.' not in string_coins:
            return string_coins + '.00'
        elif string_coins[leng - 2] == '.':
            return string_coins + '0'
        elif string_coins[leng - 3] == '.':
            return string_coins

    def get_val(self, val):
        return self.correct_str(str(round(val, 2)))
