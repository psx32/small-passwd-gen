#!/usr/bin/env python3
import secrets
import string
import PySimpleGUI as sg

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password

layout = [  [sg.Text("Password: "), sg.Input(password)],
            [sg.Exit()]]

# Create the window
window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

window.close()
