import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/

# root window
root = tk.Tk()

# configure the root window

root.geometry('300x300')
#root.resizable(True, True)
root.title('ING301 SmartHouse Dashboard')

# HeatOven control

hc_lf = ttk.LabelFrame(root, text='Heat Oven [X]')
hc_lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.W)

heater_state_var = tk.StringVar()
heater_state_var.set('Off')

heater_states = ('On', 'Off')


def heater_cmd():
    selection = "You selected the option " + heater_state_var.get()
    print(selection)


on_radio = ttk.Radiobutton(hc_lf, text='On', value='On', variable=heater_state_var, command=heater_cmd)
on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

off_radio = ttk.Radiobutton(hc_lf, text='Off', value='Off', variable=heater_state_var, command=heater_cmd)
off_radio.grid(column=1, row=0, ipadx=10, ipady=10)

# Temperature sensor control

ts_lf = ttk.LabelFrame(root, text='Temperature sensor [X]')

ts_lf.grid(column=0, row=1, padx=20, pady=20, sticky=tk.W)

temp = tk.Text(ts_lf, height=1, width=10)
temp['state'] = 'disabled'
temp.grid(column=0, row=0, padx=20, pady=20)


def refresh_temp():
    print("Refresh")


refresh_button = ttk.Button(
    ts_lf,
    text='Refresh',
    command=refresh_temp
)

refresh_button.grid(column=1, row=0, padx=20, pady=20)

#label = ttk.Label(ts_lf, text='This is a label')
#label.grid(column=1, row=0, ipadx=10, ipady=10)

root.mainloop()
