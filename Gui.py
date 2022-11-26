# This File contains GUI Elements using PySimpleGui

import PySimpleGUI as sg

from CalculatorGui import *

def runGui():
    """This GUI is responsible for the main war calulator application
    """

    # GUI Layout
    layout = [
        [sg.Text("Number of Players: "), sg.Input("2", key="NUM_PLAYERS")],
        [sg.Button("Begin", key="BEGIN"), sg.Button("Exit", key="EXIT")]
    ]

    # GUI Window
    window = sg.Window('War Calculator', layout)

    while True:
        event, values = window.read()

        # If exit is selected. Close the window
        # and break out of the polling loop
        if event == "EXIT":
            break

        # If event is begin, check window contains valid options
        if event == "BEGIN":
            try:
                begin(int(values["NUM_PLAYERS"]))
            except ValueError:
                sg.popup("You Dunce!")
                continue

        if event == sg.WIN_CLOSED:
            break

    window.close()