import tkinter as tk
from tkinter import ttk
import logging

import requests
from messaging import ActuatorState


CONNECTED = True


def lightbulb_cmd(state):

    new_state = state.get()

    logging.info(f"Dashboard: {new_state}")

    if state.get() == 'On':
        new_state = True
    else:
        new_state = False

    actuator_state = ActuatorState(new_state)

    payload = actuator_state.to_json()

    #payload = json.dumps({"state": "False"})

    headers = {'Content-Type': 'application/json'}

    url = "http://localhost:8000/smarthouse/actuator/1/current"

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


def init_lightbulb(container, did):

    lb_lf = ttk.LabelFrame(container, text=f'LightBulb [{did}]')
    lb_lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.W)

    # variable used to keep track of lightbulb state
    lightbulb_state_var = tk.StringVar(None, 'Off')

    on_radio = ttk.Radiobutton(lb_lf, text='On', value='On',
                               variable=lightbulb_state_var,
                               command=lambda: lightbulb_cmd(lightbulb_state_var))

    on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

    off_radio = ttk.Radiobutton(lb_lf, text='Off', value='Off',
                                variable=lightbulb_state_var,
                                command=lambda: lightbulb_cmd(lightbulb_state_var))

    off_radio.grid(column=1, row=0, ipadx=10, ipady=10)

    # lightbulb_state_var.set('Off')
