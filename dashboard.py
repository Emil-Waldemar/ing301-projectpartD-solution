import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/

# root window
root = tk.Tk()

# configure the root window

root.geometry('300x200')
root.resizable(False, False)
root.title('ING301 SmartHouse Dashboard')

# label frame



lf = ttk.LabelFrame(root, text='Heat Oven [X]')
lf.grid(column=0, row=0, padx=20, pady=20)

heater_state_var = tk.StringVar()
heater_state_var.set('Off')

heater_states = ('On', 'Off')


def sel():
    selection = "You selected the option " + heater_state_var.get()
    print(selection)


# create radio buttons and place them on the label frame
on_radio = ttk.Radiobutton(lf, text='On', value='On', variable=heater_state_var, command = sel)
on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

off_radio = ttk.Radiobutton(lf, text='Off', value='Off', variable=heater_state_var, command = sel)
off_radio.grid(column=1, row=0, ipadx=10, ipady=10)


root.mainloop()
