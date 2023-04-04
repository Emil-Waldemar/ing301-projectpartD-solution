import tkinter as tk

import logging

from dashboard_lightbulb import init_lightbulb
from dashboard_temperaturesensor import init_temperaturesensor

import common

# root/main window

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

root = tk.Tk()
root.geometry('300x300')
root.title('ING301 SmartHouse Dashboard')


init_lightbulb(root, common.LIGHTBULB_DID)
init_temperaturesensor(root, common.TEMPERATURE_SENSOR_DID)

root.mainloop()

# https://www.pythontutorial.net/tkinter/