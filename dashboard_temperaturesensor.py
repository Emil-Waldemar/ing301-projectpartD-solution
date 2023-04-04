import tkinter as tk
from tkinter import ttk

# device identifier for the lightbulb to be controller

# Temperature sensor control

def refresh_btn_cmd():
    print("Refresh")


def init_temperaturesensor(container, did):

    ts_lf = ttk.LabelFrame(container, text=f'Temperature sensor [{did}]')

    ts_lf.grid(column=0, row=1, padx=20, pady=20, sticky=tk.W)

    temp = tk.Text(ts_lf, height=1, width=10)
    temp['state'] = 'disabled'
    temp.grid(column=0, row=0, padx=20, pady=20)

    refresh_button = ttk.Button(ts_lf, text='Refresh', command=refresh_btn_cmd)

    refresh_button.grid(column=1, row=0, padx=20, pady=20)
