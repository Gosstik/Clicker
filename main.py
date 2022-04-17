import os
import window as win
import labels as lab
import buttons as butt

os.system('xset r off')

window = win.Window()
mylabels = lab.MyLabels(window)
buttons = butt.Buttons(window, mylabels)

mylabels.update_image()

window.wind.mainloop()

os.system('xset r on')
