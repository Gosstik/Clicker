import os
import src.window as win
import src.labels as lab
import src.buttons as butt

os.system('xset r off')

window = win.Window()

mylabels = lab.MyLabels(window)
buttons = butt.Buttons(window, mylabels)

mylabels.update_image()

window.wind.mainloop()

if mylabels.highest_score == mylabels.score:
    file = open('highest score', 'w')
    file.write(str(mylabels.highest_score))
    file.close()

os.system('xset r on')
