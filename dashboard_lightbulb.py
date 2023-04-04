import tkinter as tk
from tkinter import ttk


def lightbulb_cmd_on():

    print("ON")


def lightbulb_cmd_off():


    print("OFF")


def init_lightbulb(container, did):

    lb_lf = ttk.LabelFrame(container, text=f'LightBulb [{did}]')
    lb_lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.W)

    # variable used to keep track of lightbulb state
    lightbulb_state_var = tk.StringVar(None, 'Off')

    on_radio = ttk.Radiobutton(lb_lf, text='On', value='On', variable=lightbulb_state_var, command=lightbulb_cmd_on)
    on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

    off_radio = ttk.Radiobutton(lb_lf, text='Off', value='Off', variable=lightbulb_state_var, command=lightbulb_cmd_off)
    off_radio.grid(column=1, row=0, ipadx=10, ipady=10)
    lightbulb_state_var.set('Off')