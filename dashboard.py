import tkinter as tk

from dashboard_lightbulb import init_lightbulb
from dashboard_temperaturesensor import init_temperaturesensor

# root/main window

root = tk.Tk()
root.geometry('300x300')
root.title('ING301 SmartHouse Dashboard')

LIGHTBULB_DID = 1
TEMPERATURE_SENSOR_DID = 8

init_lightbulb(root, LIGHTBULB_DID)
init_temperaturesensor(root, TEMPERATURE_SENSOR_DID)

root.mainloop()

# https://www.pythontutorial.net/tkinter/